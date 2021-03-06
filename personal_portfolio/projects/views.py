from django.shortcuts import render

from django.shortcuts import render
from projects.models import Project

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)

# Create your views here.

def love_story(request):
    
    return render(request, 'love_story.html')

def individual(request):
    
    return render(request, 'individual.html')

def insta(request):
    
    return render(request, 'insta.html')   

def family(request):
    
    return render(request, 'family.html')     
