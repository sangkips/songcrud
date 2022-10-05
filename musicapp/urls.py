from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.listView, name='list'),
    path('detail/<int:pk>/', views.detailView, name='detail'),
    path('create/', views.creatView, name='list'),
    path('update/<int:pk>/', views.updateView, name='update'),
    path('delete//<int:pk>/', views.deleteView, name='delete'),
]