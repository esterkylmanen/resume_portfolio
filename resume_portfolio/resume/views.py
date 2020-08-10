from django.shortcuts import render, redirect
from django.contrib import messages


def resume(request):
    return render(request, "resume.html")