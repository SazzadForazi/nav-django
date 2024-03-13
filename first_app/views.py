from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("THIS IS FIRST_APP PAGE")
def courses(request):
    return HttpResponse("THIS IS FIRST_APP COURSES PAGE")
def about(request):
    return HttpResponse("THIS IS FIRST_APP ABOUT PAGE")
