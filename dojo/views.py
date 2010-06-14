from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response
from dojo.models import *

def newdojo(request):
    return render_to_response('dojo_new.html', {})

def create(request):
    dojo = Dojo(title=request.POST['title'], date=datetime.now(), finished=False)
    dojo.save()
    
    return HttpResponse('ok')