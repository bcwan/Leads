# create urls associated with frontend
from django.urls import path
from . import views

# load views index.py index
urlpatterns = [
  path('', views.index)
]