from django.db import models
import datetime

PRIORITY_CHOICES = (
	(1, 'Low'),
	(2, 'Normal'),
	(3, 'High'),
	)
class List(models.Model):
	title = models.CharField(max_length = 250, unique = True)

	def __str__(self):
		return self.title

	class Meta(object):
		"""docstring for Meta"""
		ordering = ['title']

	class Admin(object):
		"""docstring for Admin"""
		pass
			

class Item(models.Model):
	title = models.CharField(max_length=250)
	created_date = models.DateTimeField(default=datetime.datetime.now)
	priority = models.IntegerField(choices = PRIORITY_CHOICES, default=2)
	completed = models.BooleanField(default=False)
	todo_list = models.ForeignKey(List) #this is how to make foreign keys in Django
	def __str__(self):
		return self.title
	class Meta:
		ordering = ['-priority','title']

	class Admin:
		pass


