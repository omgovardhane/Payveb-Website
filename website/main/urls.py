from django.urls import path
from . import views

urlpatterns =[
#path("",views., name="index"),
path("log/",views.u_login, name="log"), #link to user login form
path("reg/", views.u_reg, name="reg"), #link to new user registeragtion form


]