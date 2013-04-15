from django.http import HttpResponse
from django.shortcuts import render

from mailclient.models import UserID

def index(request):
	latest_user_list = UserID.objects.all()
	context = {'latest_user_list': latest_user_list}
	return render(request, 'mailclient/index.html', context)

def outbox(request, user_id):
	return HttpResponse("You are looking at the outbox of User %s." % user_id)

def inbox(request, user_id):
	return HttpResponse("You are looking at the inbox of User %s."% user_id)

def newMsg(request, user_id):
	return HttpResponse("Ya'll be creatin some new message from User %s."% user_id)