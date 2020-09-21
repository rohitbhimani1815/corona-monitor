from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.Country,name="Home"),
    path("country/<str:slug>",views.state),
    path("country/<str:slug>/<str:slug1>",views.news),
    path("search",views.search),
]