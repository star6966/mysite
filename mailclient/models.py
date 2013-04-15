from django.db import models

class UserID(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=20)

	def __unicode__(self):
		return self.username

class Message(models.Model):
	to_user = models.ForeignKey(UserID, related_name="sent_to_user")
	from_user = models.ForeignKey(UserID, related_name="sent_from_user")
	title = models.CharField(max_length=50)
	msgBody = models.CharField(max_length=200)

	def __unicode__(self):
		return self.title

