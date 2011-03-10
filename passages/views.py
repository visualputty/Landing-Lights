# Create your views here.
from django.core.cache import cache
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from models import *
from django.utils import simplejson
from django.http import HttpResponse
from django.forms.models import model_to_dict

def index(request, prev=None):
    if not prev:
        prev = {}
    if not prev['form']:
        form = PassageForm()
        prev['form'] = form
    return render_to_response('passages/index.html', prev)
    
def new(request):
    response = ''
    if request.method == "POST":
        form = PassageForm(request.POST)
        if not form.is_valid():
            return redirect('index', prev={'form': form})
        new_passage = form.save()
        # Also need to try updating the VesselDetail class

        v = None
        try:
            v = VesselDetail.objects.get(ship_name=form.data['ship_name'])
        except VesselDetail.DoesNotExist:
            pass
        except VesselDetail.MultipleObjectsReturned:
            return redirect('index', prev={'form': form, 'error': 'Oops - there was a problem'})
        if not form.is_valid():
            return redirect('index', prev={'form': form, 'error': 'Oops - there was a problem'})
                                       
        form = VesselDetailForm(request.POST, instance=v)
        form.save()

        response = "Success: Your request has been received"
    form = PassageForm()
    return redirect('index', prev={'form': form, 'response': response})
    
def ajax_lookup(request):
    results = {'vessels': []}
    p = results['vessels']
    if request.method == "GET":
        if request.GET.has_key(u'q'):
            value = request.GET[u'q']
            if len(value) >= 2:
                model_results = VesselDetail.objects.filter( ship_name__istartswith=value )
                for x in model_results:
                    #p.append({'ship_name': x.ship_name})
                    p.append( model_to_dict(x) )
        json = simplejson.dumps(results)
        return HttpResponse(json, mimetype='application/json')