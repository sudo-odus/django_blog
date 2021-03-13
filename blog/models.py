from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=100,default='DEFAULT VALUE')
	content=models.TextField(default='DEFAULT VALUE')
	author=models.ForeignKey(User, on_delete=models.CASCADE,default='DEFAULT VALUE')
	date_posted=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return(self.title)

	#to tell django how to find url of any specific instance
	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})

