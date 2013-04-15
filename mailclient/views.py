from django.http import HttpResponse, Http404
from django.shortcuts import render

from mailclient.models import UserID

def index(request):
	latest_user_list = UserID.objects.all()
	context = {'latest_user_list': latest_user_list}
	return render(request, 'mailclient/index.html', context)

def outbox(request, user_id):
	try:
		user = UserID.objects.get(pk=user_id)
	except UserID.DoesNotExist:
		raise Http404
	return render(request, 'mailclient/outbox.html', {'user':user})

def inbox(request, user_id):
	try:
		user = UserID.objects.get(pk=user_id)
	except UserID.DoesNotExist:
		raise Http404
	return render(request, 'mailclient/inbox.html', {'user':user})

def newMsg(request, user_id):
	return HttpResponse("Ya'll be creatin some new message from User %s."% user_id)