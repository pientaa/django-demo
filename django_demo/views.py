from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'django_demo/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'django_demo/detail.html', {'question': question})


def results(request, question_id):
    q = Question.objects.get(pk=question_id)

    c = [str(x) for x in q.choice_set.all()]

    response = "You're looking at the results of question: %s."
    return HttpResponse(response % c)


def vote(request, question_id):
    return HttpResponse("You're voting on question: %s." % question_id)


def googleMap(request):
    if request.user.is_authenticated:
        return render(request, 'django_demo/map.html')
    else:
        return render(request, 'registration/logged_out.html')

