from django.forms import forms ,ModelForm

from core.models import Images
from .models import *

class AddQuestionForm(ModelForm):
    class Meta:
        model=Question
        fields = ['q_head','body']
        
class ImageForm(ModelForm):
    
    class Meta:
        model= Images
        fields = ['image']