from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .form import *


def home(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    education = Education.objects.all()
    experiences = Experience.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    achievements = Achievement.objects.all()
    context = {
        'education': education,
        'experiences': experiences,
        'projects': projects,
        'skills': skills,
        'achievements': achievements,
        'form': MessageForm()
    }
    return render(request, 'index.html', context)

