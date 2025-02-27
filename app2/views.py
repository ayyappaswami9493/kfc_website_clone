from django.shortcuts import render

# Create your views here.

def menu(request):
    return render(request,'menu.html')

def cart(request):
    return render(request,'cart.html')

def startorder(request):
    return render(request,'startorder.html')
