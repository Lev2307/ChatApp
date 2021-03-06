from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView
from chat.models import Chat
from .forms import RegisterForm
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'auth/profile.html'
    model = Profile
    redirect_field_name = reverse_lazy('login')

    def get(self, request, user_id, *args, **kwargs):
        self.model.id_user = user_id
        profile = get_object_or_404(self.model, user_id=self.model.id_user)
        return render(request, self.template_name, {'profile': profile, 'current_user': request.user})