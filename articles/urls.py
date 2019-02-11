from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.article_list,name="article_list"),
    path('create/',views.article_create,name="create"),
    path('<slug:slug>/',views.article_detail,name="detail"),
    path('<slug:slug>/like/',views.ArticleLikeToggle.as_view(),name="like-toggle"),
    path('<slug:slug>/api-like/',views.ArticleLikeAPIToggle.as_view(),name="like-api-toggle"),
]
