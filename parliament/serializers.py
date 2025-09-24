from rest_framework import serializers
from .models import Bill, Vote, ParliamentSession, ParliamentaryDocument

class BillSerializer(serializers.ModelSerializer):
    vote_summary = serializers.SerializerMethodField()
    
    class Meta:
        model = Bill
        fields = '__all__'
    
    def get_vote_summary(self, obj):
        votes = obj.votes.all()
        return {
            'total': votes.count(),
            'for': votes.filter(vote_choice='for').count(),
            'against': votes.filter(vote_choice='against').count(),
            'abstain': votes.filter(vote_choice='abstain').count(),
            'absent': votes.filter(vote_choice='absent').count(),
        }

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ParliamentSessionSerializer(serializers.ModelSerializer):
    bills_count = serializers.SerializerMethodField()
    
    class Meta:
        model = ParliamentSession
        fields = '__all__'
    
    def get_bills_count(self, obj):
        # Compter les projets de loi associés à cette session
        return Bill.objects.filter(submitted_date__range=[obj.start_date, obj.end_date or timezone.now().date()]).count()

class ParliamentaryDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParliamentaryDocument
        fields = '__all__'

class BillListSerializer(serializers.ModelSerializer):
    """Serializer simplifié pour la liste des projets de loi"""
    time_since_submitted = serializers.SerializerMethodField()
    
    class Meta:
        model = Bill
        fields = ['id', 'title', 'bill_number', 'status', 'category', 
                 'author', 'submitted_date', 'time_since_submitted', 'pages_count']
    
    def get_time_since_submitted(self, obj):
        from django.utils import timezone
        from django.utils.timesince import timesince
        return timesince(obj.submitted_date, timezone.now())
