from django.urls import path
from . import views

urlpatterns = [
    path("", views.analyse_mail, name="analyse_mail"),
]
