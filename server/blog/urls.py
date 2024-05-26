from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('new/', views.Blog_Create, name='create-post'),
    path('views/<int:id>',views.Views_Blog, name='views-post'),
]
