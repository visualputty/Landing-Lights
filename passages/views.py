# Create your views here.
from django.core.cache import cache
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import PassageForm

def index(request):
    form = PassageForm()
    return render_to_response('passages/index.html', { 'form': form })
    
def new(request):
    pass
    