from django.urls import path
from . import views, utils

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("random", views.randomArticle, name="random"),
    path("edit", views.edit, name="edit"),
    path("edit/send", views.sent, name="sent"),
    path("add", views.add, name="add"),
    path("search", views.search, name="search"),
    
    #   wiki items
    path("<str:name>", views.item, name="<str:name>")
]