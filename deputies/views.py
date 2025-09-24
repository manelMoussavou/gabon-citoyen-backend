from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from .models import Deputy, DeputyActivity, CitizenMessage
from .serializers import (
    DeputySerializer, DeputyActivitySerializer, 
    CitizenMessageSerializer, CitizenMessageCreateSerializer
)

User = get_user_model()

class DeputyListView(generics.ListAPIView):
    queryset = Deputy.objects.filter(is_active=True)
    serializer_class = DeputySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['party', 'circonscription']
    search_fields = ['first_name', 'last_name', 'circonscription']

class DeputyDetailView(generics.RetrieveAPIView):
    queryset = Deputy.objects.filter(is_active=True)
    serializer_class = DeputySerializer
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_deputy(request):
    """Récupérer le député de l'utilisateur connecté"""
    user = request.user
    if not user.circonscription:
        return Response(
            {'error': 'Circonscription non définie pour cet utilisateur'}, 
            status=400
        )
    
    try:
        deputy = Deputy.objects.get(
            circonscription=user.circonscription,
            is_active=True
        )
        serializer = DeputySerializer(deputy)
        return Response(serializer.data)
    except Deputy.DoesNotExist:
        return Response(
            {'error': 'Aucun député trouvé pour votre circonscription'}, 
            status=404
        )

class DeputyActivityListView(generics.ListAPIView):
    serializer_class = DeputyActivitySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['deputy', 'activity_type']
    ordering = ['-date']
    
    def get_queryset(self):
        deputy_id = self.kwargs.get('deputy_id')
        if deputy_id:
            return DeputyActivity.objects.filter(deputy_id=deputy_id)
        return DeputyActivity.objects.all()

class CitizenMessageCreateView(generics.CreateAPIView):
    queryset = CitizenMessage.objects.all()
    serializer_class = CitizenMessageCreateSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        # Ajouter des informations supplémentaires si nécessaire
        serializer.save()

class CitizenMessageListView(generics.ListAPIView):
    serializer_class = CitizenMessageSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['deputy', 'status', 'priority']
    ordering = ['-created_at']
    
    def get_queryset(self):
        deputy_id = self.kwargs.get('deputy_id')
        if deputy_id:
            return CitizenMessage.objects.filter(deputy_id=deputy_id)
        return CitizenMessage.objects.all()
