from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomePageView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        users = User.objects.all()
        return render(request, self.template_name, {'user': user, 'users': users})
