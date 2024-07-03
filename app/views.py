from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404

from app.models import CustomUser


def home_page(request):
    return render(request, 'home.html')


def dashboard(request):
    all_user = CustomUser.objects.filter(account_deleted=False)
    return render(request, 'dashboard.html', {'all_user': all_user})


def user_details(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    return render(request, 'detail.html', {'user': user})


def suspend_user(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    user.account_suspended = True
    user.save()
    return redirect('dashboard')


def delete_user(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    user.account_deleted = True
    user.save()
    return redirect('dashboard')


def deleted_users(request):
    users = CustomUser.objects.filter(account_deleted=True)  # Only show deleted users
    return render(request, 'deleted users.html', {'users': users})


def restore_user(request, pk):
    user = get_object_or_404(CustomUser, id=pk)
    user.account_deleted = False
    user.save()
    return redirect('dashboard')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "We found fraudulent Login activity, contact Support Team!")

        else:
            messages.error(request, "We found fraudulent Login activity, contact Support Team!")

    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
