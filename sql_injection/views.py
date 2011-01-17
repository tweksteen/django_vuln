from django.http import HttpResponse, HttpResponseBadRequest
from django.db import connection, transaction
from django.db.utils import DatabaseError
from django.shortcuts import render_to_response
from models import Contact

def basic(request):
    if "name" in request.GET:
        cursor = connection.cursor()
        try:
            query = "SELECT name, phone_number FROM sql_injection_contact WHERE name = '" + request.GET["name"] + "'"
            cursor.execute(query)
        except DatabaseError, e:
            return HttpResponse(e)
        row = cursor.fetchone()
        return render_to_response('sql_injection/basic.html', {'row':row})
    else:
        return HttpResponseBadRequest()
        
def advanced(request):
    if "name" in request.GET:
        c = Contact.objects.get(name=request.GET["name"])
        return render_to_response('sql_injection/advanced.html', {'contact':c})
    return HttpResponseBadRequest()
 
        