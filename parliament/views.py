from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Bill, Vote, ParliamentSession, ParliamentaryDocument
from .serializers import (
    BillSerializer, BillListSerializer, VoteSerializer, 
    ParliamentSessionSerializer, ParliamentaryDocumentSerializer
)

class BillListView(generics.ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'category']
    search_fields = ['title', 'description', 'bill_number']
    ordering_fields = ['submitted_date', 'title']
    ordering = ['-submitted_date']

class BillDetailView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

class ActiveBillsView(generics.ListAPIView):
    """Vue pour les projets de loi actifs (en débat ou en vote)"""
    serializer_class = BillListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Bill.objects.filter(status__in=['debate', 'vote'])

class RecentBillsView(generics.ListAPIView):
    """Vue pour les projets de loi récents"""
    serializer_class = BillListSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        from django.utils import timezone
        from datetime import timedelta
        
        # Projets de loi des 30 derniers jours
        thirty_days_ago = timezone.now() - timedelta(days=30)
        return Bill.objects.filter(submitted_date__gte=thirty_days_ago)

class VoteListView(generics.ListAPIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['bill', 'vote_choice']

class ParliamentSessionListView(generics.ListAPIView):
    queryset = ParliamentSession.objects.all()
    serializer_class = ParliamentSessionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering = ['-start_date']

class ParliamentaryDocumentListView(generics.ListAPIView):
    queryset = ParliamentaryDocument.objects.all()
    serializer_class = ParliamentaryDocumentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['document_type', 'bill']
    search_fields = ['title', 'description']
