from django.shortcuts import render
from .forms import AluminiForm
from.models import Alumini

# Create your views here.
def index(request):
    if request.method == "POST":
        aluminies = Alumini.objects.all()
        form = AluminiForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            form = AluminiForm()
            aluminies = Alumini.objects.all()
    else:
        form = AluminiForm()
        aluminies = Alumini.objects.all()
    params = {
        'form':form,
        'aluminies':aluminies,
    }
    return render(request,'db/index.html',params)