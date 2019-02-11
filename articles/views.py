from django.shortcuts import render,redirect
from .models import Article, Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView
from.import forms
from .forms import CommentForm
def article_list(request):
	articles = Article.objects.all().order_by('-date')
	return render(request,'article_list.html',{'articles':articles})
def article_detail(request, slug):
	article = Article.objects.get(slug=slug)
	comments = article.comments.filter(active=True, reply=None)
	if request.method == 'POST':
		comment_form =CommentForm(data=request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.article = article
			new_comment.name = request.user
			new_comment.reply_id = request.POST.get('comment_id')
			new_comment.comment_qs = None
			if new_comment.reply_id:
				new_comment.comment_qs = Comment.objects.get(id=new_comment.reply_id)
			new_comment.save()
			comment_form = CommentForm()
	else:
		comment_form = CommentForm()
	return render(request,'article_detail.html',{'article':article, 'comments':comments, 'comment_form':comment_form})
@login_required(login_url="/accounts/login/")
def article_create(request):
	if request.method=='POST':
		form=forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.author = request.user
			instance.save()
			return redirect('home')
	else:
		form=forms.CreateArticle()
	return render(request,"article_create.html",{'form':form})

class ArticleLikeToggle(RedirectView):
	def get_redirect_url(self, *args, **kwargs):
		slug = self.kwargs.get("slug")
		obj = Article.objects.get(slug=slug)
		url_=obj.get_absolute_url()
		user = self.request.user
		if user.is_authenticated:
			if user in obj.likes.all():
				obj.likes.remove(user)
			else:
				obj.likes.add(user)
		return url_ 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ArticleLikeAPIToggle(APIView):
    authentication_classes = (authentication.SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, slug=None, format=None):
        # slug = self.kwargs.get("slug")
        obj = Article.objects.get(slug=slug)
        url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked
        }
        return Response(data)