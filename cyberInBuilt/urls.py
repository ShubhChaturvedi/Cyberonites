from django import views
from django.urls import path , include
from . import views


urlpatterns = [
    path("" , views.index, name="index"),
    path("blogs" , views.blogs, name="blogs"),
    path("loginbycyberonitesstaff" , views.loginbycyberonitesstaff, name="loginbycyberonitesstaff"),
    path("handlelogin" , views.handlelogin, name="handlelogin"),
    path("addblogs" , views.addblogs, name="addblogs"),
    path("handlebaddblogs" , views.handlebaddblogs, name="handlebaddblogs"),
    path("myblogs" , views.myblogs, name="myblogs"),
    path("handlelogout" , views.handlelogout, name="handlelogout"),
    path("search" , views.search, name="search"),
    path("blogs/deletePost/tokenNo/<int:sno>" , views.deletePost, name="deletePost"),
    path("blogs/editPost/tokenNo/<int:sno>" , views.editPost, name="deletePost"),
    path("blogs/<str:slug>/", views.readmore ,name="readmore")
]