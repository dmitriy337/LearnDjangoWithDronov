from django.shortcuts import render, HttpResponse 
from .models import *

# Create your views here.
def index(request):
    return render(request, template_name='main/index.html')
    
def articles(request):

    return render(request, template_name='main/articles.html', context={'content':Posts.objects.all()})