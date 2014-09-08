from django.db import models
from django.contrib.auth.models import User
from allauth.account.signals import user_signed_up
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile')
	age = models.IntegerField(null = True)
	location = models.CharField(max_length = 50, null = True, default ="")
	display_name = models.CharField(max_length = 50, null = True, default ="")
	updated_profile = models.BooleanField(default = False)

	def __unicode__(self):
		return "{}'s profile".format(self.user.username)

@receiver(user_signed_up)
def new_user_signup(sender, **kwargs):
    p = UserProfile(user = kwargs['user'])
    p.save()