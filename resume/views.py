from django.shortcuts import render
from django.views.generic import TemplateView

#class HomeView(TemplateView):
#    template_name = 'jobs/home.html'

#def home(request):
    #return render(request, 'resume/home.html', {})

def resume(request):
    return render(request, 'resume/resume.html', {})