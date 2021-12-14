from django.db import models
from core.models import Event
# Create your models here.

class Question(Event):
    q_head = models.CharField(max_length=255)