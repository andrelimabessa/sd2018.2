from django.db import models
from django.utils import timezone

# Create your models here.
class Jogada(models.Model):
    linha = models.CharField(max_length=2)
    coluna = models.CharField(max_length=2)
    create_date = models.DateTimeField(default=timezone.now)
