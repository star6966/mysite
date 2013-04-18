from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from mailclient.models import UserID, Message

def index(request):
	latest_user_list = UserID.objects.all()
	context = {'latest_user_list': latest_user_list}
	return render(request, 'mailclient/index.html', context)

def outbox(request, user_id):
	account = get_object_or_404(UserID, pk=user_id)
	return render(request, 'mailclient/outbox.html', {'account':account})

def inbox(request, user_id):
	account = get_object_or_404(UserID, pk=user_id)
	return render(request, 'mailclient/inbox.html', {'account':account})

def new_message(request, user_id):
	account = get_object_or_404(UserID, pk=user_id)
	latest_user_list = UserID.objects.all()
	context = {'latest_user_list': latest_user_list,'account':account}
	return render(request, 'mailclient/create.html', context)

def send(request, user_id):
	account = get_object_or_404(UserID, pk=user_id)
	body = request.POST['body']
	to_user = get_object_or_404(UserID, pk=request.POST['to_user'])
	title = request.POST['title']
	m = Message(to_user = to_user, from_user = account, title = title, msgBody = body)
	m.save()
	return render(request, 'mailclient/inbox.html', {'account':account})