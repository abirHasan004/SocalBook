from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
 path('',home),
 path('signup',Signup,name='signup'),
 path('signin',SignIn ,name='signin'),
 path('profile/<str:pk>',profileView,name='profile'),
 path('logout',Logout,name='logout'),
 path('Accountsettings',AccountSettings,name='setting'),
 path('informationUpload',InformationUpdate,name='Information'),
 path('Like_Post',LikePost,name='LikePost'),
 path('Follower',follower,name='follower')
]
 
