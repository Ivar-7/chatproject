from django.shortcuts import render, redirect
from .models import Room, Message
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {'username': username, 'room_details': room_details, 'room': room})

def checkroom(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    room_id = request.POST['room_id']
    username = request.POST['username']
    message = request.POST['message']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('<h1>Message sent successfully</h1>')