from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Hoot, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def loginUser(request):
    error = None
    if request.method == 'POST':
        form = request.POST
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)
        if user == None:
            error = 'Username or Password is incorrect!'
        else:
            login(request, user)    
            return redirect('users:dashboard')

    return render(request, 'users/login.html', {"error": error} )

def signup(request):
    error = None
    if request.method == 'POST':
        form = request.POST
        first_name = form['firstname']
        last_name = form['lastname']
        user_name = form['username']
        email = form['email']
        password = form['password']
        password2 = form['password2']

        if User.objects.filter(username=user_name).exists():
            error = "User name is already in use!"

        elif User.objects.filter(email=email).exists():
            error = "That email already in use!"    
        
        elif password != password2:
            error = "Passwords do not match!"
        else:
            user = User.objects.create_user(username=user_name, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        return redirect('users:login')

    return render(request, 'users/signup.html', {'error': error})
@login_required
def dashboard(request):

    hoots = Hoot.objects.filter(author=request.user).order_by('created_date')

    context = {
        "hoots": hoots
    }
    return render(request, 'users/dashboard.html', context)
@login_required
def logoutUser(request):
    logout(request)
    return redirect('blog:index')


  