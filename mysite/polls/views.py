from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
   
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)    
   return render(request, 'polls/detail.html', {'question':question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice"
        })  
    else:
        selected_choice.votes +=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))  

def add_question(request):
    print(f'METHOD: {request.method}')
    if request.method == "GET":
        return render(request, 'polls/add_question.html')
    elif request.method == 'POST':
        question = question(question_text=request.post['question'], pub_date=timezone.now())
        question.save()
        form = request.POST
        for key in form:
            if key.startswith('choice'):
                if form[key]:
                    choice = choice(question=question, choice_text=request.POST[key])
                    choice.save()
        return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))            
