from django.urls import path

from public_chat.views import(
    public_chat_view,
    public_chat_delete,
)

app_name = 'public_chat'

urlpatterns = [
    path('<room_id>/', public_chat_view, name='view'),
    path('<room_id>/delete', public_chat_delete, name='delete'),
]