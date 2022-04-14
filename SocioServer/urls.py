from re import template
from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from personal.views import (
	home_screen_view,
)

from account.views import (
    RegisterView,
    LoginView,
    LogoutView,
    AccountSearchView,
)

from public_chat.views import(
    public_chat_create,
    my_chat_rooms,
)

urlpatterns = [
	path('', home_screen_view, name='home'),
    path('create/', public_chat_create, name="create"),
    path('rooms/', my_chat_rooms, name="rooms"),
    path('public_chat/', include('public_chat.urls', namespace='public-chat')),
    path('account/', include('account.urls', namespace='account')),
	path('admin/', admin.site.urls),
    path('chat/', include('chat.urls', namespace='chat')),
    path('friend/', include('friend.urls', namespace='friend')),
    path('login/', LoginView, name="login"),
    path('logout/', LogoutView, name="logout"),
    path('register/', RegisterView, name="register"),
    path('search/', AccountSearchView, name="search"),

    # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)