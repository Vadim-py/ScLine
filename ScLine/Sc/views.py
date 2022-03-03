from django.shortcuts import render
from .forms import *


def index(request):
    return render(request, 'index.html')

def sclineNew(request):
    form = ScLineUsr()
    return render(request, '', {'form': form})