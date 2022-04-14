from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.conf import settings

from public_chat.models import PublicChatRoom

DEBUG = False

def public_chat_view(request, room_id):

    context = {}

    try:
        room = PublicChatRoom.objects.get(id=room_id)
        context['room_id'] = room_id
        context['room'] = room
    except PublicChatRoom.DoesNotExist:
        return HttpResponse("Room doesn't exist.")

    context['debug_mode'] = settings.DEBUG
    context['debug'] = DEBUG

    return render(request, f"public_chat/public_chat_rooms.html", context)

def public_chat_create(request):
    
    user = request.user

    context = {}

    if user.is_authenticated:
        if request.POST:
            title = request.POST.get('title')
            description = request.POST.get('description')

            try:
                room = PublicChatRoom.objects.get(title=title)

                if room:
                    context['error'] = 'Room with this title already exist. Please choose another title.'

            except PublicChatRoom.DoesNotExist:

                PublicChatRoom.objects.create(author=user, title=title, description=description)
                return redirect('home')
    else:
        return redirect('login')

    return render(request, "public_chat/create_public_chat.html", context)

def my_chat_rooms(request):
    user = request.user
    
    context = {}

    if user.is_authenticated:
        try:
            rooms = PublicChatRoom.objects.filter(author=user)
            context['rooms'] = rooms
            context['user'] = user
        except PublicChatRoom.DoesNotExist:
            return HttpResponse("You don't own any public chat rooms yet.")
    else:
        return redirect('login')

    return render(request, "public_chat/my_public_chat_rooms.html", context)

def public_chat_delete(request, room_id):
    
    user = request.user

    if user.is_authenticated:
        room = PublicChatRoom.objects.get(id=room_id)

        if user.id == room.author.id:
            PublicChatRoom.objects.get(id=room_id).delete()
        else:
            return HttpResponse("You can only delete your own room.")
    else:
        return redirect('login')

    return redirect('home')
