from django.urls import path 
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name='create'),
    path('detail/<int:blog_id>/', views.detail, name='detail'),
    path('delete/<int:blog_id>/', views.delete_blog, name='delete'),
    path('comment/<int:blog_id>/', views.comment, name='comment'),
    path('like/', views.like, name='like')


]