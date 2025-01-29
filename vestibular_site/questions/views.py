from django.shortcuts import render
from .models import Question

def question_list(request):
    questions = Question.objects.all()  # Busca todas as questões no banco de dados
    return render(request, 'questions/list.html', {'questions': questions})