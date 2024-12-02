from django.shortcuts import render 
from django.http import HttpResponse
from datetime import datetime
from django.urls import reverse

def home(request):
    return render (request, 'home/index.html')
    #return HttpResponse({'Today': datetime.today()})