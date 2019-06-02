from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.urls import reverse
from .models import Question

def index(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	template=loader.get_template('polls/index.html')
	context={'latest_question_list':latest_question_list,}
	return HttpResponse(template.render(context, request))

'''polls,index.html 템플릿을 불러온 후, context를 전달.
context: 템플릿에서 쓰는 변수명과 python 객체를 연결하는 dict값'''

def detail(request, question_id):
	try:
		question=Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("질문이 존재하지 않습니다")
	return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})

def vote(request, question_id):
	question=get_object_or_404(Question, pk=question_id)
	try:
		selected_choice=question.choice_set.get(pk=request.POST['choice'])
	except(KeyError, Choice.DoesNotExist):
		return render(request,'polls/detail.html',{
		'question':question,
		'error_message':"선택지를 선택하지 않았어요.",
		})
	else:
		selected_choice.votes+=1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
