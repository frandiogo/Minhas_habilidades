from django.db import models

class Question(models.Model):
    SUBJECT_CHOICES = [
        ('MAT', 'Matemática'),
        ('FIS', 'Física'),
        ('QUI', 'Química'),
        ('BIO', 'Biologia'),
        ('HIS', 'História'),
    ]
    DIFFICULTY_CHOICES = [
        ('F', 'Fácil'),
        ('M', 'Médio'),
        ('D', 'Difícil'),
    ]

    statement = models.TextField(verbose_name="Enunciado")
    alternatives = models.JSONField(verbose_name="Alternativas")  # Ex: {"A": "Opção 1", "B": "Opção 2", ...}
    answer = models.CharField(max_length=1, verbose_name="Gabarito")
    subject = models.CharField(max_length=3, choices=SUBJECT_CHOICES, verbose_name="Matéria")
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY_CHOICES, verbose_name="Dificuldade")

    def __str__(self):
        return self.statement