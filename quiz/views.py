from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    quiz=Quiz.objects.all()
    return render(request,'home.html',{'quiz':quiz})