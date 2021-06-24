from django.urls import path
from .views import index, about, show_category, add_category, add_page

app_name = 'xxx'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('category/<slug:category_name_slug>/', show_category, name='show_category'),
    path('add_category/', add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', add_page, name='add_page'),
]