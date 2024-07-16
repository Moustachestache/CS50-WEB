from django.shortcuts import render, HttpResponse, redirect
from django.http import Http404
from django import forms
from . import utils
import markdown2
import random
import sys

# Create your views here.

def index(request):
    return render(request, "index.htm", {"entries": utils.list_entries})

def randomArticle(request):
    if len(utils.list_entries()) == 0:
        return HttpResponse("<center>looks like there arent any entries ... <a href=\"add\">create one?</a><br /><a href=\"/\">back</a></center>")
    else:
        return redirect(item, random.choice(utils.list_entries()))

def edit(request):
    name = request.GET.get("i", "")
    data = utils.get_entry(name)
    if not name or name == "":
        return HttpResponse("aaaaaaaaaaaaaaaaaaa")
    elif not data:
        return HttpResponse("lets create this bitch")
    return render(request, "edit.htm", {
            "info": data, 
            "name" : name})

def item(request, name):
    data = utils.get_entry(name)
    if data != None:
        return render(request, "item.htm", {"info":  markdown2.markdown(data), "name": name})
    else:
        return HttpResponse("<center>looks like the entry doesnt exist ... <a href=\"add\">let's create it?</a><br /><a href=\"/\">back</a></center>")

def add(request):
    return render(request, "add.htm")

def sent(request):
    # process
    id = request.POST.get("name")
    data = request.POST.get("data")
    if id and data:
        if request.GET.get("s", ""):
            utils.save_entry(id, data)
        else:
            return HttpResponse("<center>this article already exists<br /><a href=\"/\">back</a></center>")
        # redirect to page
    return redirect(item, id)

def search(request):
    id = request.POST.get("search")
    entries = list("")
    if not id:
        return redirect(index)
    for entry in utils.list_entries():
        print("debug: " + entry, file=sys.stderr)
        if entry == id:
            return redirect(item, entry)
        elif id in entry:
            entries.append(entry)
    if not entries:
        return HttpResponse("couldnt find anything<br /><a href=\"/\">back</a>")
    else:
        return render(request, "index.htm", {"entries": entries})