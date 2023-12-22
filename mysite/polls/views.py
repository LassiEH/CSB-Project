from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader
from django.views import generic
from django.urls import reverse
from .models import Question, Choice, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name ='polls/detail.html'

    def get(self, request, *args, **kwargs):
        question = self.get_object()
        comments = Comment.objects.filter(question=question)
        form = CommentForm()
        return render(request, self.template_name, {'question': question, 'comments': comments, 'form': form})

    def post(self, request, *args, **kwargs):
        question = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.question = question
            new_comment.save()
        return self.get(request, *args, **kwargs)

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
{
    'question': question,
    'error_message': "You didn't select a choice."
})
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
    #return HttpResponse("You're voting on question %s." % question_id)

def create_comment(request):
    if request.method == 'POST':
        comment_text = request.POST('comment_text')
        new_comment = Comment.objects.create(user=request.user, comment_text=comment_text)

        return render(request, 'polls/detail.html', {'comment': new_comment})
    else:
        return render(request, 'polls/create_comment.html')