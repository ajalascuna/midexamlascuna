from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate
from .forms import CandidateModelForm

# Create your views here.

def index(request):
    context = {}
    candidates = Candidate.objects.all()
    context['candidates'] = candidates
    return render(request, 'index.html', context)

def candidate_detail(request, candidate_id):
    context={}
    context['candidate'] = Candidate.objects.get(id=candidate_id)
    return render(request, 'detail.html', context)

def vote(request):
    context = {}
    candidates = Candidate.objects.get(id=candidate_id)
    candidate.votes.all().count
    context['candidates'] = candidates
    return render(request, 'index.html', context)

def candidate_update(request, candidate_id):
    context = {}
    title = Candidate.objects.get(id=candidate_id)

    if request.method == 'POST':
        form = CandidateModelForm(request.POST, instance=title)
        if form.is_valid():
            form.save()
            return HttpResponse('Candidate updated.')
        else:
            context['form'] = form
            render(request, 'candidate_update.html', context)
    else:
        context['form'] = CandidateModelForm(instance=title)
    return render(request, 'candidate_update.html', context)
