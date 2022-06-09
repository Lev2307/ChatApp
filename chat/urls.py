from django.urls import path

from .views import (
    ChatRoomView
)

urlpatterns = [
    path('chat_room/<int:chatroom_id>/', ChatRoomView.as_view(), name="login"),
]