from django.contrib import admin
from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
   path('',home,name="home"),
   path('signup',signup,name="signup"),
   path('signin',signin,name="signin"),
   path('signout',signout,name="signout"),
   path('page2',page2,name='page2'),
   path('add_booklet',add_booklet_view,name="add_booklet"),
   path('delete/<int:id>/',delete,name='delete'),
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
