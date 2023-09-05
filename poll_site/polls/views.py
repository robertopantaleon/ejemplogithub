from django.urls import reverse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Survey, Choice, Question


# Create your views here.
def index(request):
    # questions = Question.objects.all()
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # elfilter es un where
    surveys = Survey.objects.filter(active=True).order_by("-pub_date")[:5]
    # output = ', '.join([q.question_text for q in questions])
    # template = loader.get_template("polls/index.html")
    context = {
        "mensaje": "Lista de ultimas 5 encuestas",
        "latest_surveys": surveys,
    }
    return render(request, "polls/index.html", context)
    # response = template.render(context, request)
    # return HttpResponse(response) Paso 8 y 9


# return HttpResponse(template.render(context, request))


def detail(request, survey_id):
    try:
        questions = Question.objects.filter(survey=survey_id)
    except Question.DoesNotExist:
        print("Aqui se puede meter un logger")
        raise Http404("La pregunta no existe")
    context = {
        "mensaje": "Preguntas de la encuesta",
        "questions": questions,
        "survey_id": survey_id,
    }
    # Quitar la ruta de polls
    # return render(request, "polls/detail.html", context)
    return render(request, "polls/detail.html", context)


def results(request, survey_id):
    question = get_object_or_404(Question, pk=survey_id)
    return render(request, "polls/results.html", {"question": question})
    # return HttpResponse("Results for question %s" % question_id)

    # (Question, pk=question_id)
    # return render(request, "polls/results.html", {"question": question})
    # return render(request, "results.html", {"question": question})


def vote(request, survey_id):
    question = get_object_or_404(Question, pk=survey_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
