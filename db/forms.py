from django.forms import ModelForm
from .models import Alumini

class AluminiForm(ModelForm):
    class Meta:
        model = Alumini
        fields = ['name', 'designation', 'profile']
