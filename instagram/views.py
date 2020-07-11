from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")
    
def profile(request):
    context = {}
    return render(request, 'instagram/profile.html', context) 

