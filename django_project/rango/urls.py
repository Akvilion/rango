from django.urls import path
from .views import one, about


urlpatterns = [
    path('', one, name='index'),
    path('about/', about, name='about'),
]