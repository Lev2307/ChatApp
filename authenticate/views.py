from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from .forms import RegisterForm
from .models import Profile

# Create your views here.

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.save()
        user_info = Profile(user=user)
        user_info.save()
        return redirect('/auth/login')

class LoginView(LoginView):
    template_name = 'auth/login.html'
    success_url = reverse_lazy('/')

class LogoutView(LogoutView):
    redirect_field_name = reverse_lazy("index")
    template_name = "index.html"

class ProfileView(DetailView):
    template_name = 'auth/profile.html'
    model = Profile

    def get(self, request, user_id, *args, **kwargs):
        Profile.id_user = user_id
        current_user = request.user
        profile = get_object_or_404(Profile, user_id=Profile.id_user)
        return render(request, self.template_name, {'profile': profile, 'current_user': current_user})