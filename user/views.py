from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insta-profile')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form}) 