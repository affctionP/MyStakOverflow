from django.db import models
from .fields import AudioField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
# Create your models here.

class  Event(models.Model):
    body    =models.TextField()
    creted  =models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract=True


def media_storge(instance, filename):
    path = 'event/{0}/{1}/{2}'.format(instance.content_object.id,instance.__class__.__name__,filename)
    return path
class Media(models.Model):
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    #event = models.ForeignKey('Event',on_delete=models.CASCADE)

class Images(Media)  :
    image = models.ImageField(upload_to=media_storge)

class Voice(Media):
    voice_file=AudioField(upload_to=media_storge)
    
