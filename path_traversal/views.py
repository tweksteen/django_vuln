import os
import mimetypes
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound
from django.shortcuts import render_to_response
from utils import official_cleaning

def basic(request):
    if "file" in request.GET:
        fullpath = os.path.join("static", request.GET["file"])
        if not os.path.exists(fullpath) or os.path.isdir(fullpath):
            return HttpResponseNotFound()
        mimetype, encoding = mimetypes.guess_type(fullpath)
        mimetype = mimetype or 'application/octet-stream'
        contents = open(fullpath, 'rb').read()
        response = HttpResponse(contents, mimetype=mimetype)
        response["Content-Length"] = len(contents)
        if encoding:
            response["Content-Encoding"] = encoding
        return response
    else:
        return HttpResponseBadRequest()

def advanced(request):
    if "file" in request.GET:
        redirect, cleaned_path = official_cleaning(request.GET["file"])
        if redirect:
            HttpResponseBadRequest()
        fullpath = os.path.join("static", cleaned_path)
        if not os.path.exists(fullpath) or os.path.isdir(fullpath):
            return HttpResponseNotFound()
        mimetype, encoding = mimetypes.guess_type(fullpath)
        mimetype = mimetype or 'application/octet-stream'
        contents = open(fullpath, 'rb').read()
        response = HttpResponse(contents, mimetype=mimetype)
        response["Content-Length"] = len(contents)
        if encoding:
            response["Content-Encoding"] = encoding
        return response
    else:
        return HttpResponseBadRequest()