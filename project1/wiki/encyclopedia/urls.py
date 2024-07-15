from django.urls import path
from . import views, utils

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("random", views.random, name="random"),
    path("edit", views.edit, name="edit"),
    
    #   wiki items
    path("<str:name>", views.item, name="<str:name>")
]