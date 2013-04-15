from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from mailclient.models import UserID

def index(request):
	latest_user_list = UserID.objects.all()
	context = {'latest_user_list': latest_user_list}
	return render(request, 'mailclient/index.html', context)

def outbox(request, user_id):
	user = get_object_or_404(UserID, pk=user_id)
	return render(request, 'mailclient/outbox.html', {'user':user})

def inbox(request, user_id):
	user = get_object_or_404(UserID, pk=user_id)
	return render(request, 'mailclient/inbox.html', {'user':user})

def new_message(request, user_id):
	return HttpResponse("Ya'll be creatin some new message from User %s."% user_id)