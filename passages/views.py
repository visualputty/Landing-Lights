# Create your views here.
from django.core.cache import cache
from django.views.generic.simple import direct_to_template
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from models import *
from django.utils import simplejson
from django.forms.models import model_to_dict

def index(request):
    rCxt = RequestContext(request)
    if request.method == "POST":
        # Been sent some information
        form = PassageForm(request.POST)
        if form.is_valid():
            # Also need to try updating the VesselDetail class
            v = None
            try:
                v = VesselDetail.objects.get(ship_name=form.data['ship_name'])
            except VesselDetail.DoesNotExist:
                pass
            except VesselDetail.MultipleObjectsReturned:
                request.flash.now['error'] = "Oops - there was a problem there."
                return render_to_response('passages/index.html', {'form': form}, context_instance=rCxt)
            vForm = VesselDetailForm(request.POST, instance=v)
            if vForm.is_valid():
                vForm.save()
                form.save()
                request.flash['success'] = "Success: Your request has been received"
                return HttpResponseRedirect('/')
            else:
                request.flash.now['error'] = 'Oops - there was an error here.'
                return render_to_response('passages/index.html', {'form': form}, context_instance=rCxt)

        else:
            # In this case we failed validation
            request.flash.now['error'] = "Oops = there was an error with your form."
        return render_to_response('passages/index.html', {'form': form}, context_instance=rCxt)
    
    else:
        # Need a fresh form
        form = PassageForm()
        return render_to_response('passages/index.html', {'form': form}, context_instance=rCxt)
        
    
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