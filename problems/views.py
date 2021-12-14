
from django.http import HttpResponse, JsonResponse
from django.forms.models import modelform_factory
from django.shortcuts import render ,HttpResponse,get_object_or_404
from django.views.generic import TemplateView ,FormView ,ListView,DetailView
from .forms import *
from .models import Question
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.forms import modelformset_factory
# Create your views here.

class index(TemplateView):
    template_name = 'index.html'
    
class addQuestionView(TemplateView):
    template_name = 'addq_form.html'
    

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            #ImageformSet=modelformset_factory(Images,form=ImageForm ,extra=2)
            imgeform=ImageForm()
            questionform=AddQuestionForm()
            #formset = ImageformSet()
            context ={'imgeform':imgeform, 'questionform': questionform}
            return self.render_to_response(context=context)
        else :
            pass #redirect to login
    
        
    def post(self, request, *args, **kwargs):
        questionform=AddQuestionForm(request.POST)
        if questionform.is_valid():
            my_file=request.FILES.getlist('file')
            
            q_data=questionform.cleaned_data
            q=Question(q_head=q_data['q_head'],body=q_data['body'])
            q.save()
            for i in my_file :
                img=Images(image=i,content_object=q)
                img.save()
        return JsonResponse({'post':'false'})
    
    
    
class QuestionList(ListView):
    model=Question
    template_name='q_list.html'
    
    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        
            
class QuestionDetail(DetailView) :
    model=Question
    template_name='q_detail.html' 
    def get_object(self):
        slug = self.kwargs.get('pk')
        return get_object_or_404(Question, pk=slug) 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj =self.get_object()
        rel=GenericRelation(Images,related_query_name='Question')
        context['images'] = Images.objects.filter(object_id=obj.id,
                                         content_type=ContentType.objects.get_for_model(obj).id)
        
        for i in context['images']:
            print ()
        return context    
    
 
