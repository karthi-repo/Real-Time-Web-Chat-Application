from django.http.response import HttpResponse
from django.shortcuts import render
from django.conf import settings

from public_chat.models import PublicChatRoom

DEBUG = False

def home_screen_view(request):

	rooms = PublicChatRoom.objects.all()

	context = {}

	context['debug_mode'] = settings.DEBUG
	context['debug'] = DEBUG
	context['room_id'] = "1"
	context['rooms'] = rooms

	user = request.user

	if user.is_authenticated:

		try:
			room = PublicChatRoom.objects.filter(author=user)
			context['my_room'] = room
			context['user'] = user
		except PublicChatRoom.DoesNotExist:
			pass

	return render(request, "personal/home.html", context)