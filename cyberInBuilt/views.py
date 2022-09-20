import json
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Staff , Post
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    staff = Staff.objects.all()
    params = {"staff" : staff}
    return render(request , 'index.html' , params)

def blogs(request):
    posts = Post.objects.all()
    params ={"posts":posts}
    return render(request, 'blogs.html',params)

def readmore(request,slug):
    post = Post.objects.filter(slug=slug).first()
    isAuthUser=(str(post.author)==str(request.user))
    params = {'post':post, 'isAuthUser':isAuthUser}
    return render(request, 'readmore.html',params)

def loginbycyberonitesstaff(request):
    return render(request, 'login.html')

def handlelogin(request):
    if request.method == 'POST':

        #Getting User Info

        username = request.POST['loginusername']
        password = request.POST['loginpassword']

        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            # return HttpResponse("Loggedin")
            messages.success(request, "Successfully Logged In")
            return redirect("/myblogs")

        else:
            # messages.success(request, "Account Do Not Exist!")
            return redirect('/loginbycyberonitesstaff')

    else:
        return HttpResponse("404 Not found")

def addblogs(request):
    return render(request, 'addblogs.html')
    

def handlebaddblogs(request):
    if request.method == 'POST' and request.FILES['image']:
        title = request.POST['title']
        content = request.POST['content']
        upload = request.FILES['image']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        slug= str(request.user) + "_Post=" + str(len(Post.objects.filter(author = request.user)) + 1)
        blogfields = Post(author=request.user, title= title, content=content, image=file, slug=slug)
        blogfields.save()
        return redirect("/blogs/"+slug)

def myblogs(request):
    posts = Post.objects.filter(author=request.user)
    params = {'posts':posts} 
    return render(request,"myblogs.html",params)

def handlelogout(request):
    logout(request)
    return redirect("/#home")

def deletePost(request,sno):
    blogSno = Post.objects.filter(sno=sno)
    blogSno.delete()
    return redirect("/myblogs")

def editPost(request,sno):
    blogSno = Post.objects.filter(sno=sno)

def search(request):
    query = request.GET['query']
    if len(query)>78:
        posts = []
    
    else:
        all_blogs_title = Post.objects.filter(title__icontains=query)
        all_blogs_content = Post.objects.filter(content__icontains=query)
        all_blogs_author = Post.objects.filter(author__icontains=query)
        posts = all_blogs_author.union(all_blogs_title.union(all_blogs_content))
        # messages.error(request, "No search Results Found")
    params = {'posts':posts,'query':query}
    return render(request, 'blogs.html',params)