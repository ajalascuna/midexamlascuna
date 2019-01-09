from django.forms import ModelForm
from .models import Candidate

class CandidateModelForm(ModelForm):
    class Meta:
        model = Candidate
        exclude = ['id']
