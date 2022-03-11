from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UserRegisterForm
from django.core.mail import send_mail

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')

            # ::::::::Send Mail Code:::::::::::::
            send_mail(
                'Account Created',
                f'An account has been created for you. Your username is {username}',
                settings.EMAIL_HOST_USER,
                ['email', 'kabinbasnet22@gmail.com'],
                fail_silently=False,
            )

            return redirect('login')

    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')
