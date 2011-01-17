import re
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response

def basic(request):
    if "name" in request.GET:
        return render_to_response('xss/basic.html', {'name':request.GET["name"]})
    else:
        return HttpResponseBadRequest()

def stripped(request):
    if "name" in request.GET:
        name = request.GET["name"].replace("<script>", "").replace("</script>", "")
        return render_to_response('xss/stripped.html', {'name':name})
    else:
        return HttpResponseBadRequest()
        
def js_based(request):
    if "name" in request.GET:
        return render_to_response('xss/js_based.html', {'name':request.GET["name"]})
    else:
        return HttpResponseBadRequest()
        
def dom_based(request):
    if "name" in request.GET:
        return render_to_response('xss/dom_based.html', {'name':request.GET["name"]})
    else:
        return HttpResponseBadRequest()