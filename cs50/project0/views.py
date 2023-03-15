from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, "project0/index.html")

def imageSearch(request):
    return render (request, "project0/imageSearch.html")

def advancedSearch(request):
    return render (request, "project0/advancedSearch.html")