from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages # success, error, info, warning
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account is created! You are now able to login')        
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class MyLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_url = 'blog-home'
    success_message = 'You are successfully logged in!'

class MyLogoutView(SuccessMessageMixin, LogoutView):
    template_name = 'users/logout.html'
    success_url = 'blog-home'
    
    def dispatch(self, request, *args, **kwargs): # mora ovako jer nije form view
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.INFO, 'Successfully logged out.')
        return response