from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article
def homepage(request,template='path/to/templates'):
	context = {
	    'articles': Article.objects.all().order_by('-date'),
    }
	#return HttpResponse('homepage')
	return render(request,'homepage.html',context)
def about(request):
	#return HttpResponse('about')
	return render(request,'about.html')
def contact(request):
	return render(request,'contact.html')