from django.shortcuts import render,redirect
from .forms import FacebookLoginForm
# Create your views here.

def login(request):
    if request.method == 'POST':
        form = FacebookLoginForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data (or authenticate if this is a login form)
            return redirect('login')  # Adjust this to the correct redirect path after login
    else:
        form = FacebookLoginForm()
    
    return render(request, 'login.html', {'form': form})
