from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render_to_response
from django.template import RequestContext

def basic(request):
    try:
        import libxml2
    except ImportError:
        return HttpResponse("Please install libxml2 to play with XPath injection")
    if "name" in request.POST:
        name = request.POST['name']
        doc = libxml2.parseFile('xpath_injection/credential.xml')
        results = doc.xpathEval("//Account[UserName/text()='" + name + "']/FirstName/text()")
        if results:
            result = str(results[0])
        else:
            result = ""
        return render_to_response('xpath_injection/basic.html', {'result':result, 'name':name},
                context_instance=RequestContext(request))
    else:
        return render_to_response('xpath_injection/basic.html', 
                context_instance=RequestContext(request))