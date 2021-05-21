from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('table/', views.table, name='blog-table'),
    path('data/', views.data, name='blog-data'),

]