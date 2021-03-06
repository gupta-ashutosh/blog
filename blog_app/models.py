from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

class Category(models.Model):
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		# return reverse('post-detail', args=(str(self.id)))
		return reverse('home')


class Post(models.Model):
	title = models.CharField(max_length=255)
	title_tag = models.CharField(max_length=255, default="")
	introduction = models.TextField(default = '')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = RichTextField(blank=True, null=True)
	post_date = models.DateField(auto_now_add = True)
	category = models.CharField(max_length=255, default='')
	# category = models.ManyToManyField(Category, blank=True, null=True, through='PostCategory')

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		#return reverse('post-detail', args=(str(self.id)))
		return reverse('home')

# class PostCategory(models.Model):
# 	post = models.ForeignKey(Post, on_delete=models.CASCADE)
# 	category = models.ForeignKey(Category, on_delete=models.CASCADE)
