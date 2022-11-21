from django.shortcuts import HttpResponse, render

# Create your views here.
def about(Request):
    return HttpResponse('this is about page')
def customer(Request):
    return HttpResponse('customer page')
def Home(Request):
    return HttpResponse('Home page')