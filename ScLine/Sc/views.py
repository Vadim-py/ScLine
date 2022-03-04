from django.shortcuts import render
from .forms import *


def index(request):
    return render(request, 'index.html')

def sclineNew(request):
    form = ScLineUsrForm()
    return render(request, 'ScForm.html', {'form': form})