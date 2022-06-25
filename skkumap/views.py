from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def main(request):
    if request.user.is_authenticated:
        return render(request, 'main.html')
    else:
        return redirect('login')

def loading(request):
    return render(request, 'loading.html')

def onboarding(request):
    return render(request, 'onboarding.html')