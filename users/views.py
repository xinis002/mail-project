from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import UserRegistrationForm, UserUpdateForm, UserLoginForm


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация прошла успешно!")
            return redirect("profile")
    else:
        form = UserRegistrationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваш профиль был обновлен.")
            return redirect("users:profile")
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, "registration/profile.html", {"form": form})


class CustomLoginView(LoginView):
    authentication_form = UserLoginForm
    template_name = "registration/login.html"

    def form_valid(self, form):

        messages.success(self.request, "Вы успешно вошли в систему!")
        return super().form_valid(form)
