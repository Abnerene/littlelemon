from django.contrib import admin 
from django.urls import path 
from .views import sayHello 
from . import views
  
urlpatterns = [ 
    path('', views.index, name='index'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
]