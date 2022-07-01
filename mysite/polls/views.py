#from django.http import HttpResponse
from django.shortcuts import render
from .models import List

def index(request):
    if request.method=="POST":
        print (request.POST)
        name=request.POST["name"]
        sex=request.POST["sex"]
        bench=request.POST["bench"]
        dead=request.POST["dead"]
        squart=request.POST["squart"]
        weight=request.POST["weight"]
        
        elist= List(name=name,sex=sex,bench=bench,dead=dead,squart=squart,weight=weight)
        elist.save()
    return render(request,'polls\webp.html')

# Create your views here.
