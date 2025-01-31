# core/views.py
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'admin' and password == '123':  # Simulação de login
            return redirect('home')
    return render(request, 'core/login.html')

def home_view(request):
    return render(request, 'core/home.html')