from django.urls import path
from .views import index, about, show_category, add_category


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('category/<slug:category_name_slug>/', show_category, name='show_category'),
    path('add_category/', add_category, name='add_category'),
]