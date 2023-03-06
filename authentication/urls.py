from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.loginpage,name='login'),
    path('users/',views.usersu,name='usersuccess'),
    path('signup/',views.signup,name="signup"),
    path('check/',views.check,name="check"),
    path('signup_user/',views.signup_user,name="signup_user"),
    path('home/',views.home,name="home"),
    path('history/',views.history,name="history"),
    path('logout/',views.Logoutpage,name="logout"),
    path('adhome/',views.adhome,name="adhome"),
    path('aproved/',views.aprroved,name="aproved"),
    path('entry/',views.adentry,name="entry"),
    path('adhome/delete/<int:id>',views.dell),
    path('adhome/fetch/<int:id>',views.approve),
    path('history/<int:id>',views.edit),
    path('profile/',views.profile,name="profile"),
    path('user_home/',views.user_home,name="user_home")
      
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)