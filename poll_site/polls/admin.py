from django.contrib import admin
from .models import Survey, Question, Choice

# Register your models here.
# admin.site.register(Survey)
# admin.site.register(Question)
# admin.site.register(Choice)


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "survey")
    inlines = [ChoiceInline]


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
