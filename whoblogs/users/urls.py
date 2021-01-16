from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.loginUser, name='login' ),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logoutUser, name='logout'),
    

]        