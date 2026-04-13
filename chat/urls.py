from django.urls import path
from .views import chat_page, chat_api

urlpatterns = [
    path("chat/", chat_page, name="chat"),
    path("chat-api/", chat_api, name="chat_api"),
]