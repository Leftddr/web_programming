from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    # 테이블을 담을 모델을 선언한다.
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    # 테이블을 담을 모델을 선언한다.
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    # Qusetion에 쿼리를 던져서 pk가 question_id인것을 받아온다.
    # question_id는 params로 던진 url이다.
    question = get_object_or_404(Question, pk=question_id)
    try:
        #choice_set은 장고만의 특징으로, 참조된 테이블을 조회할때 _set을 붙여 사용한다.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        # .save()함수는 부모로부터 오버라이딩 된 함수이다. => 테이블을 저장하게 해준다.
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #reverse 함수를 사용하면 polls의 question.id로 이동한다. => names = results로 설정해 놓은곳에 <int:pk>에 인수를 전달하며 redirect한다.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))