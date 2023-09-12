from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from .models import Customer
from .forms import logininfo
# Create your views here.

def home(request):
    return render(request,"./MPR/document.html")

def login_page(request):
    form=logininfo()
    if request.method=="POST":
        form=logininfo(request.POST)
        if form.is_valid():
            user=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            phone=form.cleaned_data["number"]
            email=form.cleaned_data["mail"]
            Customer.objects.create(username=user,password=password,mail=email,phone=phone)
            return HttpResponseRedirect("thank-you")
    return render(request,"./MPR/login_page.html",{"form":form})

def thank_you(request):
    return render(request,"MPR/thx.html")

def bathroom(request):
    return HttpResponse("this is for bathroom tiles")
def kitchen(request):
    return HttpResponse("this is for kitchen tiles")
def washroom(request):
    return HttpResponse("this is for washroom tiles")
def livingroom(request):
    return HttpResponse("this is for living room tiles")
def elevation(request):
    return HttpResponse("this is for elevation tiles")
def bedroom(request):
    return HttpResponse("this is for bedroom tiles")
def commercial(request):
    return HttpResponse("this is for commercial tiles")
def parking(request):
    return HttpResponse("this is for parking tiles")
def washbasine(request):
    return HttpResponse("this is for washbasine tiles")
def pod(request):
    return HttpResponse("this is for pods ")
def premiumfloor(request):
    return HttpResponse("this is for premium range tiles")
def premiumwall(request):
    return HttpResponse("this is for premium range tiles")
def premiumelevation(request):
    return HttpResponse("this is for premium elevation tiles")
def vitrified_tiles(request):
    return HttpResponse("this is for premium vitrified tiles")
def GVT_tiles(request):
    return HttpResponse("this for GVT premium tiles")