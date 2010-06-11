# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response
from home.models import *

def index(request):
    dojos = Dojo.all()
    return render_to_response('home_index.html', {'dojos':dojos})

