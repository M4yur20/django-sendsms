from django.contrib import admin
from django.urls import path
from . import views
app_name = 'sms'

urlpatterns = [
    path('send/',views.sendsms_view,name='sends'),
    path('success/',views.success_view,name='success'),
]
