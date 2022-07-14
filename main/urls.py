from django.urls import path
from .views import *

app_name = 'main'
urlpatterns = [
    path('', main_index, name="index"),
    path('about/', main_about, name="about"),
    path('vr-videos/', main_virtual, name="vr-videos"),
    path('contacts/', main_contacts, name="contacts"),
    path('help/', main_help, name="help"),
    path('support/', main_support, name="support"),
    path('add/', main_add, name="add"),
    path('delete/', main_delete, name='delete'),
]
