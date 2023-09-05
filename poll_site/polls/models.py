from django.db import models


# Create your models here.
class Survey(models.Model):
    # campos de tipo String y de longitud mazima de 200
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    pub_date = models.DateTimeField("date published")
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# Tabla Question
class Question(models.Model):
    # campos de tipo String y de longitud mazima de 200
    # question_text = models.CharField(max_length=200)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # regrese el nombre de la pregunta
    def __str__(self):
        return self.text


# tabla con 3 campos
class Choice(models.Model):
    # Lave foranea, si se borra la pregunta se borran las respuestas.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.text
