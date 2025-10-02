# analyser/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="analyser_index"),
    path("api/analyse/", views.analyse_mail_api, name="analyse_api"),
]
