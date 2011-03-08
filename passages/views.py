# Create your views here.
from django.core.cache import cache
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import *
from django.utils import simplejson
from django.http import HttpResponse

def index(request):
    form = PassageForm()
    return render_to_response('passages/index.html', { 'form': form })
    
def new(request):
    pass
    
def ajax_lookup(request):
    results = {'vessels': []}
    p = results['vessels']
    if request.method == "GET":
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            if len(value) > 2:
                model_results = VesselDetail.objects.filter( ship_name__istartswith=value )
                for x in model_results:
                    p.append({'ship_name': x.ship_name})
        json = simplejson.dumps(results)
        return HttpResponse(json, mimetype='application/json')