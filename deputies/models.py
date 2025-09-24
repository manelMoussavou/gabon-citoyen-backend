from django.db import models

class Deputy(models.Model):
    """Modèle pour les députés"""
    
    PARTY_CHOICES = [
        ('independent', 'Indépendant'),
        ('pdg', 'PDG'),
        ('rn', 'Rassemblement National'),
        ('upp', 'Union du Peuple Patriote'),
        ('other', 'Autre'),
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200, editable=False)
    party = models.CharField(max_length=20, choices=PARTY_CHOICES)
    circonscription = models.CharField(max_length=200)
    mandate_start = models.DateField()
    mandate_end = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    
    # Informations personnelles
    birth_date = models.DateField(blank=True, null=True)
    biography = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='deputies/', blank=True, null=True)
    
    # Coordonnées
    contact_email = models.EmailField(blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    office_address = models.TextField(blank=True)
    
    # Métadonnées
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Député"
        verbose_name_plural = "Députés"
        ordering = ['last_name', 'first_name']
    
    def save(self, *args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.circonscription}"

class DeputyActivity(models.Model):
    """Modèle pour l'activité des députés"""
    
    ACTIVITY_TYPES = [
        ('proposal', 'Proposition de loi'),
        ('amendment', 'Amendement'),
        ('question', 'Question parlementaire'),
        ('intervention', 'Intervention'),
        ('meeting', 'Réunion de travail'),
        ('citizen_response', 'Réponse aux citoyens'),
        ('other', 'Autre'),
    ]
    
    deputy = models.ForeignKey(Deputy, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateTimeField()
    bill_related = models.ForeignKey('parliament.Bill', on_delete=models.CASCADE, blank=True, null=True)
    
    class Meta:
        verbose_name = "Activité de député"
        verbose_name_plural = "Activités de députés"
        ordering = ['-date']
    
    def __str__(self):
        return f"{self.deputy.full_name} - {self.title}"

class CitizenMessage(models.Model):
    """Modèle pour les messages des citoyens aux députés"""
    
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('in_progress', 'En cours de traitement'),
        ('responded', 'Répondu'),
        ('closed', 'Fermé'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Basse'),
        ('medium', 'Moyenne'),
        ('high', 'Haute'),
        ('urgent', 'Urgente'),
    ]
    
    deputy = models.ForeignKey(Deputy, on_delete=models.CASCADE, related_name='citizen_messages')
    sender_name = models.CharField(max_length=200)
    sender_email = models.EmailField()
    sender_phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    
    # Réponse
    response = models.TextField(blank=True)
    response_date = models.DateTimeField(blank=True, null=True)
    
    # Métadonnées
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Message citoyen"
        verbose_name_plural = "Messages citoyens"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.sender_name} -> {self.deputy.full_name}: {self.subject}"
