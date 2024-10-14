from django.urls import path

from .views import enpoint,avocate_details,list_avocates

urlpatterns = [

    path("",enpoint,name="enpoint"),

    path("list_avocates", list_avocates, name="list_avocates"),


    
    path("details/<int:pk>/",avocate_details,name="avo_details"),
    

    
]
