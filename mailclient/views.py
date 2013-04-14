from django.http import HttpResponse

def index(request):
	return HttpResponse("Hola, I am Steve the Webpage. How are you?")

def outbox(request, user_id):
	return HttpResponse("You are looking at the outbox of User %s." % user_id)

def inbox(request, user_id):
	return HttpResponse("You are looking at the inbox of User %s."% user_id)

def newMsg(request, user_id):
	return HttpResponse("Ya'll be creatin some new message from User %s."% user_id)