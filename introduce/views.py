from django.shortcuts import render
from introduce.models import AccessLog

# Create your views here.
def introduce_view(request):
    
    access_log = AccessLog()
    access_log.location = 'introduce'
    access_log.save()
    
    return render(request, 'index.html')

    # AccessLog.objects.create(
    #     location = 'introduce'
    # )
    