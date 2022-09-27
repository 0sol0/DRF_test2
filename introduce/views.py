from django.shortcuts import render
from . import models

# Create your views here.
def introduce_view(request):
    return render(request, 'index.html')
