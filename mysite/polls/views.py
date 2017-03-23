from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question


# Create your views here.

def index(request):
# version 0

# version 1
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)

# version 2
#    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))

# version 3
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
# version 0    
#    return HttpResponse("You're looking at question %s." % question_id)

# version 1
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'polls/detail.html', {'question': question})

# version 2
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# ejemplos de HTTPResponse: escribiendo un texto derecho viejo
# >>> from django.http import HttpResponse
# >>> response = HttpResponse("Here's the text of the Web page.")
# >>> response = HttpResponse("Text only, please.", content_type="text/plain")

# ejemplos de ir escribiendo la respuesta
# >>> response = HttpResponse()
# >>> response.write("<p>Here's the text of the Web page.</p>")
# >>> response.write("<p>Here's another paragraph.</p>")

# a partir de django 10: 
# si necesitas hacer steraming usa:  StreamingHttpResponse
# los objetos iterados, van a ser parseados como string y descartados.
# https://docs.djangoproject.com/en/1.10/ref/request-response/#django.http.HttpResponse 

# para  agreagar parametros al header de la response
# >>> response = HttpResponse()
# >>> response['Age'] = 120
# >>> del response['Age']

# para responder un archivo
# response = HttpResponse(my_data, content_type='application/vnd.ms-excel')
# >>> response['Content-Disposition'] = 'attachment; filename="foo.xls"'

