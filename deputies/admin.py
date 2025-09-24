from django.contrib import admin
from .models import Deputy, DeputyActivity, CitizenMessage

@admin.register(Deputy)
class DeputyAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'party', 'circonscription', 'is_active', 'mandate_start']
    list_filter = ['party', 'is_active', 'mandate_start']
    search_fields = ['first_name', 'last_name', 'circonscription']
    ordering = ['last_name', 'first_name']
    readonly_fields = ['full_name', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('first_name', 'last_name', 'full_name', 'birth_date', 'profile_picture')
        }),
        ('Informations politiques', {
            'fields': ('party', 'circonscription', 'mandate_start', 'mandate_end', 'is_active')
        }),
        ('Contact', {
            'fields': ('contact_email', 'contact_phone', 'office_address')
        }),
        ('Biographie', {
            'fields': ('biography',)
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(DeputyActivity)
class DeputyActivityAdmin(admin.ModelAdmin):
    list_display = ['deputy', 'activity_type', 'title', 'date']
    list_filter = ['activity_type', 'date', 'deputy']
    search_fields = ['title', 'description', 'deputy__first_name', 'deputy__last_name']
    ordering = ['-date']
    date_hierarchy = 'date'

@admin.register(CitizenMessage)
class CitizenMessageAdmin(admin.ModelAdmin):
    list_display = ['sender_name', 'deputy', 'subject', 'status', 'priority', 'created_at']
    list_filter = ['status', 'priority', 'created_at', 'deputy']
    search_fields = ['sender_name', 'sender_email', 'subject', 'message']
    ordering = ['-created_at']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Expéditeur', {
            'fields': ('sender_name', 'sender_email', 'sender_phone')
        }),
        ('Message', {
            'fields': ('deputy', 'subject', 'message', 'priority')
        }),
        ('Traitement', {
            'fields': ('status', 'response', 'response_date')
        }),
        ('Métadonnées', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
