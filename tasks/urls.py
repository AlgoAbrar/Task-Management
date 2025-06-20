from django.contrib import admin
from django.urls import path
from tasks.views import home
from tasks.views import contact
from .views import showtask,show_taska

urlpatterns = [
    path('showtask/', showtask)
    path('show_task/<id>',show_task)
]



""




















