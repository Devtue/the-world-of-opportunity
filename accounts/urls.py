from django.urls import path
from.import views
from django.contrib.auth import views as p_views


urlpatterns=[
	path('signup/',views.signup_view,name="signup"),
	path('login/',views.login_view,name="login"),
	path('logout/',views.logout_view,name="logout"),
	path('password-change/',p_views.PasswordChangeView.as_view(),name='password_change'),
	path('password-change/done/',p_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
]