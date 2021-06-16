from django.shortcuts import render
from .models import Category


def index(request):
    category_list = Category.objects.all()
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    a=1
    context_dict = {'about': 'about'}
    return render(request, 'rango/about.html', context=context_dict)
