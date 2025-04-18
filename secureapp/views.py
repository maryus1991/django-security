from django.shortcuts import render ,redirect ,reverse
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm


def main(request):
    return render(request, 'index.html')

def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect(reverse('two_factor:login'))

    return render(request, 'register.html', {'form': form})

@login_required()
def dashboard(request):
    return render(request, 'dashboard.html')

def user_logout(request):
    auth.logout(request)
    return redirect(reverse('main'))