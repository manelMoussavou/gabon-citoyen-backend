from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Bill(models.Model):
    """Modèle pour les projets de loi"""
    
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('submitted', 'Soumis'),
        ('debate', 'En débat'),
        ('vote', 'En vote'),
        ('passed', 'Adopté'),
        ('rejected', 'Rejeté'),
        ('enacted', 'Promulgué'),
    ]
    
    CATEGORY_CHOICES = [
        ('agriculture', 'Agriculture'),
        ('economy', 'Économie'),
        ('education', 'Éducation'),
        ('health', 'Santé'),
        ('digital', 'Numérique'),
        ('environment', 'Environnement'),
        ('justice', 'Justice'),
        ('defense', 'Défense'),
        ('social', 'Social'),
        ('infrastructure', 'Infrastructure'),
        ('other', 'Autre'),
    ]
    
    title = models.CharField(max_length=300)
    bill_number = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    full_text = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    author = models.CharField(max_length=200)  # Auteur du projet (ministère, député, etc.)
    submitted_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    vote_date = models.DateTimeField(blank=True, null=True)
    pages_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-submitted_date']
    
    def __str__(self):
        return f"{self.bill_number} - {self.title}"

class Vote(models.Model):
    """Modèle pour les votes sur les projets de loi"""
    
    VOTE_CHOICES = [
        ('for', 'Pour'),
        ('against', 'Contre'),
        ('abstain', 'Abstention'),
        ('absent', 'Absent'),
    ]
    
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='votes')
    deputy_name = models.CharField(max_length=200)
    vote_choice = models.CharField(max_length=10, choices=VOTE_CHOICES)
    vote_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['bill', 'deputy_name']
    
    def __str__(self):
        return f"{self.deputy_name} - {self.bill.title} - {self.get_vote_choice_display()}"

class ParliamentSession(models.Model):
    """Modèle pour les sessions parlementaires"""
    
    SESSION_TYPES = [
        ('ordinary', 'Session ordinaire'),
        ('extraordinary', 'Session extraordinaire'),
    ]
    
    name = models.CharField(max_length=100)
    session_type = models.CharField(max_length=20, choices=SESSION_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-start_date']
    
    def __str__(self):
        return f"{self.name} ({self.get_session_type_display()})"

class ParliamentaryDocument(models.Model):
    """Modèle pour les documents parlementaires"""
    
    DOCUMENT_TYPES = [
        ('bill', 'Projet de loi'),
        ('amendment', 'Amendement'),
        ('report', 'Rapport'),
        ('minutes', 'Compte-rendu'),
        ('other', 'Autre'),
    ]
    
    title = models.CharField(max_length=300)
    document_type = models.CharField(max_length=20, choices=DOCUMENT_TYPES)
    file = models.FileField(upload_to='parliamentary_documents/')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='documents', blank=True, null=True)
    session = models.ForeignKey(ParliamentSession, on_delete=models.CASCADE, related_name='documents', blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-upload_date']
    
    def __str__(self):
        return self.title
