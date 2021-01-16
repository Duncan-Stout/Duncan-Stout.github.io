from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {
        'message': 'My first solo app!!'
    }
    return render(request, 'snap/index.html', context)