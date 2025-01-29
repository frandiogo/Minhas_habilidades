from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Painel de administração
    path('', include('questions.urls')),  # Inclui as URLs do app "questions"
]