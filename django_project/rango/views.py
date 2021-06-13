from django.shortcuts import render

# Create your views here.

def one(request):
    return render(request, 'rango/index.html')