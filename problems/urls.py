from django.urls import path

from problems.views import addQuestionView
from .views import *
app_name='problems'
urlpatterns = [

path ('add',addQuestionView.as_view(),name='add-q'),
    path('list',QuestionList.as_view(),name='q-list'),
    path('<int:pk>',QuestionDetail.as_view(),name='q-detail'),

    
    
]
