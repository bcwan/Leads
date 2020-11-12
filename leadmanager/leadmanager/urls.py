from django.contrib import admin
from django.urls import path, include

# include directs all data sent in / route to 'leads.url'
urlpatterns = [
    path('', include('leads.urls')),
]
