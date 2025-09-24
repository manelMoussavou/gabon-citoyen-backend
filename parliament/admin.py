from django.contrib import admin
from .models import Bill, Vote, ParliamentSession, ParliamentaryDocument

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['bill_number', 'title', 'status', 'category', 'author', 'submitted_date']
    list_filter = ['status', 'category', 'submitted_date']
    search_fields = ['title', 'bill_number', 'author']
    ordering = ['-submitted_date']
    readonly_fields = ['submitted_date', 'last_updated']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['bill', 'deputy_name', 'vote_choice', 'vote_date']
    list_filter = ['vote_choice', 'vote_date']
    search_fields = ['deputy_name', 'bill__title']
    ordering = ['-vote_date']

@admin.register(ParliamentSession)
class ParliamentSessionAdmin(admin.ModelAdmin):
    list_display = ['name', 'session_type', 'start_date', 'end_date', 'is_active']
    list_filter = ['session_type', 'is_active', 'start_date']
    search_fields = ['name', 'description']
    ordering = ['-start_date']

@admin.register(ParliamentaryDocument)
class ParliamentaryDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'document_type', 'bill', 'session', 'upload_date']
    list_filter = ['document_type', 'upload_date']
    search_fields = ['title', 'description']
    ordering = ['-upload_date']
