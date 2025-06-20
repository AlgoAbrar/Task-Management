from django.contrib import admin
from django.urls import path
from tasks.views import home
from tasks.views import contact
from .views import show_task

urlpatterns = [
    path('show-task/', show_task)
]



""




















