from django.shortcuts import get_object_or_404, render
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic.detail import SingleObjectMixin



from .models import Question
from .models import Project
'''

class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'latest_question_list'
    paginate_by = 5

    def get_queryset(self):
	    i=0
	    x=i+5

	    """
	    Return the last five published questions (not including those set to be
	    published in the future).
	    """
	    return Question.objects.filter( 
	    	pub_date__lte=timezone.now()
	    ).order_by('-pub_date')
'''

class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ProjectView(generic.DetailView):
    template_name = 'portfolio/project_detail.html'



    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
        return context    

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Project.objects.filter(pub_date__lte=timezone.now())
        # projectDetail_list = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        #return render(request, 'portfolio/project_list.html', {'project': projects})    

class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'project_list'
    

    def get_queryset(self):
        

        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Project.objects.filter( 
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())



class ResultsView(generic.DetailView):
    model = Question
    template_name = 'portfolio/results.html'

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'portfolio/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('portfolio:results', args=(p.id,)))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'portfolio/detail.html', {'question': question})

    '''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'portfolio/index.html', context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'portfolio/results.html', {'question': question})
'''

def project_list(request):
    project_list = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portfolio/project_list.html', {'project': projects})

def projectDetail_list(request):
    projectDetail_list = Project.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portfolio/project_list.html', {'project': projects})    

