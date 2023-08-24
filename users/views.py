from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateFrom, ProfileUpdateForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={"form": form})


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateFrom(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES,  instance=request.user.profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated.')
            return redirect('/profile')
    else:
        user_form = UserUpdateFrom(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
   
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'users/profile.html', context=context)
