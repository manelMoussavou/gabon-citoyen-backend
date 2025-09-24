from rest_framework import serializers
from .models import Deputy, DeputyActivity, CitizenMessage

class DeputySerializer(serializers.ModelSerializer):
    activity_count = serializers.SerializerMethodField()
    recent_activities = serializers.SerializerMethodField()
    
    class Meta:
        model = Deputy
        fields = '__all__'
    
    def get_activity_count(self, obj):
        from django.utils import timezone
        from datetime import timedelta
        
        # Activités des 30 derniers jours
        thirty_days_ago = timezone.now() - timedelta(days=30)
        return obj.activities.filter(date__gte=thirty_days_ago).count()
    
    def get_recent_activities(self, obj):
        recent_activities = obj.activities.all()[:5]
        return DeputyActivitySerializer(recent_activities, many=True).data

class DeputyActivitySerializer(serializers.ModelSerializer):
    activity_type_display = serializers.CharField(source='get_activity_type_display', read_only=True)
    
    class Meta:
        model = DeputyActivity
        fields = '__all__'

class CitizenMessageSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    priority_display = serializers.CharField(source='get_priority_display', read_only=True)
    
    class Meta:
        model = CitizenMessage
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')

class CitizenMessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CitizenMessage
        fields = ['deputy', 'sender_name', 'sender_email', 'sender_phone', 
                 'subject', 'message', 'priority']
