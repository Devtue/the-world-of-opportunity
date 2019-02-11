from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
class Article(models.Model):
	"""docstring for Article"""
	title  = models.CharField(max_length=100)
	slug   = models.SlugField()
	body   = models.TextField()
	date   = models.DateTimeField(auto_now_add=True)
	thumb  = models.FileField(blank=True)
	url    = models.CharField(max_length=255,null=True, blank=True)
	author = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE)
	likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True ,related_name='article_likes')

	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:150] + '.....' 
	def get_absolute_url(self):
		return reverse('detail',kwargs={"slug": self.slug})
	def get_like_url(self):
		return reverse('like-toggle', kwargs={"slug": self.slug})
	def get_api_like_url(self):
		return reverse('like-api-toggle', kwargs={"slug": self.slug})

class Comment(models.Model):
	article = models.ForeignKey(Article,on_delete=models.CASCADE, related_name='comments')
	name = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE,related_name='comments_creator')
	body = models.TextField()
	reply = models.ForeignKey('Comment', null = True , on_delete=models.CASCADE , related_name= 'replies')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)
	class Meta:
		ordering = ('created',)
	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.article)