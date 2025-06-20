from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # work with database
    # Data Transform
    # Data Visualization
    # Data PAss
    # Http Response / JSON Response
    return HttpResponse("Hello, world. You're at the home page.")

def contact(request):
    return HttpResponse("<h1 style='color:red'>Contact us page</h1>")

def show_task(request):
    return HttpResponse(" This is task page") 