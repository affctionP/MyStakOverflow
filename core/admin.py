from django.contrib import admin
from django.db.models import fields
from .models import *
# Register your models here.
class inline (admin.StackedInline):
    model = Images
    fields =('image',)


admin.site.register(Images)