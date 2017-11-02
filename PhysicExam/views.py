from django.shortcuts import render
from PhysicExam.models import QUESTION
from PhysicExam.models import answer
from django.http import HttpResponse
from django.template import Context,loader
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def  home(request):
    physicdisp=QUESTION.objects.all()
    answerdisp=answer.objects.all()
    x=loader.get_template('My templates\home.html')
    y=Context({'physicdisp':physicdisp},{'answerdisp':answerdisp})
    return HttpResponse(x.render(y))
# Create your views here.
