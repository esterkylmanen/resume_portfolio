from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import RequestContext
from .models import Contact, Education, Experience, Skill

def resume(request):
    contact_list = Contact.objects.all()
    # contact_dict = {'contacts': contact_list}
    
    edu_list = Education.objects.all()
    # edu_dict = {'educations': edu_list}
    
    return render(request, 'resume.html', {'contacts' : contact_list, 'educations' : edu_list})

def contact(request):
    contact_list = Contact.objects.all()
    contact_dict = {'contacts': contact_list}
    
    return render(request, 'contact.html', contact_dict)


def portfolio(request):
    contact_list = Contact.objects.all()
    # contact_dict = {'contacts': contact_list}
    
    edu_list = Education.objects.all()
    # edu_dict = {'educations': edu_list}
    
    return render(request, 'portfolio.html', {'contacts' : contact_list, 'educations' : edu_list})

