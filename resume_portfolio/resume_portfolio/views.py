from django.shortcuts import render, redirect
from django.contrib import messages


def resume_portfolio(request):
    return render(request, "resume_portfolio.html")