from django.shortcuts import render

# Create your views here.
def introduce_view(request):
    return render(request, 'index.html')