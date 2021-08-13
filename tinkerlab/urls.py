"""tinkerlab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from tinkerlab import settings
from home.forms import Passreset,Passconfirm

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="home"),
    path("signup/",views.signup, name="signup"),
    path("loginuser/",views.loginuser, name="login"),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='pass_reset.html',form_class=Passreset),name="passreset"),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='pass_reset_done.html'),name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='pass_reset_confirm.html',form_class=Passconfirm),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='pass_reset_compalate.html'),name="password_reset_complete"),
    
    path("signout/",views.signout, name="logout"),
    path("forum/",views.forum, name="forum"),
    path('postcomment/',views.postcommentss,name="postcoment"),
    path("profile/",views.profile, name="profile"),
    path("filter1/",views.filter1, name="filter1"),
    path("filter2/",views.filter2, name="filter2"),
    path("deletepost/",views.deletepost, name="deletepost"),
    path("deletepost2/",views.deletepost2, name="deletepost2"),


    path("about-us/",views.about, name="about"),
    path("events/",views.events, name="events"),
    path("notify/",views.notify, name="notify"),





]+ static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
