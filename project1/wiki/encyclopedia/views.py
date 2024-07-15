from django.shortcuts import render, HttpResponse
from django.http import Http404
from django import forms
from . import utils
import markdown2

# Create your views here.
def index(request):
    return render(request, "index.htm", {"entries": utils.list_entries})

def random(request):
    return HttpResponse("random")

def edit(request):
    name = request.GET["i"]
    data = utils.get_entry(name)
    if not name:
        return render(request, "index.htm", {"entries": utils.list_entries})
    if data:
        return render(request, "edit.htm", {
            "info": data, 
            "name" : name})
    else:
        return HttpResponse("create")

def item(request, name):
    data = utils.get_entry(name)
    if data != None:
        return render(request, "item.htm", {"info":  markdown2.markdown(data), "name": name})
    else:
        return HttpResponse("couldnt find item maybe we shud create it :)))")