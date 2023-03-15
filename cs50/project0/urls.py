from . import views
from django.urls import path

app_name="project0"

urlpatterns = [
    path("", views.index, name="index"),
    path("imageSearch", views.imageSearch, name="imageSearch"),
    path("advancedSearch", views.advancedSearch, name="advancedSearch"),
    
]