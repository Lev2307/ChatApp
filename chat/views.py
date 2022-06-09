from django.shortcuts import get_object_or_404, render
from django.views import View
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chat
from authenticate.models import Profile

# Create your views here.
class HomePageView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        users = User.objects.all()
        return render(request, self.template_name, {'user': user, 'users': users})

class ChatRoomView(LoginRequiredMixin, DetailView):
    model = Chat
    template_name = 'chat/chat_room.html'

    def get(self, request, chatroom_id, *args, **kwargs):
        self_user = request.user
        self.model.room_id = chatroom_id
        return render(request, self.template_name)
