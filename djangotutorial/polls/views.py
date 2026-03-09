# from django.shortcuts import render <- Esto seria lo normal

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import Question


# Imprimimos con shortcut
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}

    return render(request, "polls/index.html", context)
"""
# Imprimimos SIN shortcut: lo mismo pero mas farragoso
def detail(request, question_id):
    pregunta = get_object_or_404(Question, pk=question_id)
    plantilla = loader.get_template("polls/detail.html")
    contexto = {"incognita": pregunta}

    return HttpResponse(plantilla.render(contexto, request))

# Mucho mas reducido, pero misma funcionalidad
"""
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})




def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
