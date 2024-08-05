from django.db import models
class Affectation(models.Model):
    codeaffectation=models.IntegerField()
    intituler=models.CharField(max_length=30)
    def __str__(self):
        return self.intituler
    
    
class User_info(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    codeaffectation=models.ForeignKey(Affectation, on_delete=models.CASCADE, null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
# Create your models here.
import datetime
class User(models.Model):
    STATUS_CHOICES = [
        ('NOUVEAU', 'nouveau'),
        ('EN INSTANCE', 'en instance'),
        ('EN COURS DE TRAITEMENT', 'en cours de traitement'),
        ('TRAITER', 'traiter'),
        ('CLOTURE', 'cloture'),

    ]
    TYPE_CHOICES = [
        ('MATERIEL', 'materiel'),
        ('LOGICIEL', 'logiciel'),
    ]
    user = models.ForeignKey(User_info, on_delete=models.CASCADE,null=True)
    description=models.CharField(max_length=300)
    type= models.CharField(max_length=30,choices=TYPE_CHOICES, default='MATERIEL')
    selection = models.CharField(max_length=30)
    date_of_Add = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='NOUVEAU')
    response = models.TextField(blank=True, null=True)
    date_de_changement=models.DateField(default=datetime.date.today,null=True)

    def __str__(self):
        return self.description
    


class GrpsUser(models.Model):
    GROUPENAME_CHOICES = [
        ('ADMIN', 'admin'),
        ('UTILISATEUR', 'utilisateur'),
    ]
    group_name = models.CharField(max_length=30, choices=GROUPENAME_CHOICES, null=True)
    descriptiongrps = models.TextField(blank=True)

    def __str__(self):
        return self.group_name

class Hbilitation(models.Model):
    user = models.ForeignKey(User_info, on_delete=models.CASCADE, null=True)
    permission = models.CharField(max_length=50)
    granted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} - {self.permission}"

class UserGroup(models.Model):
    user = models.ForeignKey(User_info, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(GrpsUser, on_delete=models.CASCADE, null=True)

    class Meta:
        unique_together = ('user', 'group')

    def __str__(self):
        return f"{self.user.name} - {self.group.group_name}"
    
from django.db import models

class ChatMessage(models.Model):
    user = models.ForeignKey(User_info, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)  # True si le message vient de l'admin
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {'Admin' if self.is_admin else self.user.name} at {self.timestamp}"
    