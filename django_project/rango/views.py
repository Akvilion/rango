from django.shortcuts import render

# Create your views here.

def one(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'about': 'about'}
    return render(request, 'rango/about.html', context=context_dict)