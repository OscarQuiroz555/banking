from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Banking App")


def Country(request):
    return HttpResponse("List of Countries")

def Department(request):
    return HttpResponse("List of Departments")

def City(request):
    return HttpResponse("List of Cities")

