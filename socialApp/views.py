import json
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import  *
from django.http import JsonResponse
from .forms import Forms
# Create your views here
@login_required(login_url='signin')
def home(request):
    if request.method=='POST':
        if 'POST' in request.POST:
            img1=request.FILES['myFile']
            caption=request.POST.get('caption')
            print(img1,caption)
            print(img1,caption)
            if img1== None:
                messages.error(request,'upload a image')
            else:
                post=POST.objects.create(img=img1,Captions=caption,user_id=request.user.id).save()
            # postFrom=Forms(request.POST,request.FILES) 
            # print('hello')
            # if postFrom.is_valid():
                 
            #     postFrom.save()
                 
            # else:
            #     print(postFrom.errors.as_data(),request.FILES,request.POST)
            #     print('somthing is wrong',request.FILES)
           #     messages.error(request,'your data is not valid')
    post=[] 
    profiles=[]      
    follower_check=FollowerCount.objects.filter(Follower=request.user)
    user_profile=profile.objects.filter(user=request.user.id).first()
    for follower in follower_check:
        user=User.objects.get(username=follower.user)
        post=POST.objects.filter(user_id=user.id).order_by('-created_at')
        profiles=profile.objects.filter(user=user.id).first()  
         
      
    # print(post)
    # for x in post: 
    #      y=0
     
         
    # y=0
    # post2=[]
    # for x in post:
    #      post1=POST.objects.filter(user_id=request.user.id).order_by('-created_at')[y]
    #      post2.append(post1)
    #      y+=1
          
    context={
        'post':list(post),
        'form':Forms,
        'profile': profiles,
        'user_profile':user_profile
        }   
      
        # print(post2,'hello world',post,'hello',y)
    return  render(request,'index.html',context)
     
    
     
     

def Signup(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('Email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        print(request.POST)
        

        # User.objects.filter(id=12).delete()
        if User.objects.filter(username=name).exists():
             messages.error(request,'user name already taken') 
        if User.objects.filter(email=email).exists():
              messages.error(request,'Email is already exists plz login')
        if password1=='':
             messages.error(request,'plz enter a valid password')
        elif name=='':
            messages.error(request,'plz enter a vaild password')
        elif email=='':
            messages.error(request,'plz enter a valid password')
        elif password1==password2:            
            User.objects.create(username=name,password=password1,email=email)
            messages.success(request,'Your signup is complete plz login') 
            user=User.objects.get(username=name, password=password1)
            login(request,user)
            # return redirect(InformationUpdate)           
         
    return render(request,'signup.html')



def InformationUpdate(request):
    
    try:
        img=request.POST.get('image')
        bio=request.POST.get('bio')
        location=request.POST.get('location')
        if bio == '':
            messages.error(request,'enter a bio')
        if img == '':
            img='default-avatar-icon-of-social-media-user-vector.jpg'
            profile.objects.create(profileimg=img,bio=bio,loc=location,user_id=request.user.id)
        else:
            profile.objects.create(profileimg=img,bio=bio,loc=location,user_id=request.user.id)
    except IntegrityError:
        messages.error(request,'your informtion is already uploaded')
        return  redirect(SignIn)
    return render(request,'setting.html')    

 

def SignIn(request):
    try:
        if request.method=="POST":
            print('hello')
            name=request.POST.get('username')
            password=request.POST.get('password')
            print(name,password)
            user=User.objects.get(username=name, password=password)
            
            if user is not None:
                print(name,password)
                login(request, user)
                return redirect(home)
 
    
    except User.DoesNotExist: 
       messages.error(request,'Wrong Infromations')  
       print('hello world')  
        
    return render(request,'signin.html')

def Logout(request):
     logout(request)
     return redirect(SignIn)

@login_required(login_url='signin')
def profileView(request,pk):
     
    user=User.objects.get(username=pk)
    post=POST.objects.filter(user=user.id)
    post_count=len(post)
    print(request.POST)
    Profile=profile.objects.filter(user=user.id).first()
    follower_check=FollowerCount.objects.filter(user=pk,Follower=request.user).first()
    context={
      'user':user,
      'post':post,
      'post_count':post_count,
      "profile":Profile,
      'follower_check':follower_check,
      "request_user":str(request.user)
    }
    return render(request,'profile.html',context)
    
    
@login_required(login_url='signin')
def AccountSettings(request):
     
    if request.user.is_authenticated:
        try:
            if request.method=='POST':
                img=request.FILES['image']
                bio=request.POST.get('bio')
                location=request.POST.get('location')
                profileCreate=profile.objects.filter(user_id=request.user.id).first()
                if bio == '':
                    messages.error(request,'enter a bio')
                if img == '':
                    img='default-avatar-icon-of-social-media-user-vector.jpg'
                    profilemodel=profile.objects.filter(user_id=request.user.id).first()
                    profilemodel.profileimg=img
                    profilemodel.bio=bio
                    profilemodel.loc=location
                    profilemodel.save()
                    return redirect(home)
                elif profileCreate == None:
                    profile.objects.create(profileimg=img,bio=bio,loc=location,user_id=request.user.id)
                    return redirect(home)
                else:
                    profilemodel=profile.objects.filter(user_id=request.user.id).first()
                    profilemodel.profileimg=img
                    profilemodel.bio=bio
                    profilemodel.loc=location
                    profilemodel.save()
                    return redirect(home)
        except IntegrityError:
            messages.error(request,'your informtion is already uploaded')
            return  redirect(home)
    else:
        return redirect(Signup)  

    return render(request,'setting.html')
  
@login_required(login_url='signin')
def follower(request):
    if request.method =='POST':
        
        user=request.POST['user']
        follower=request.POST['follower']
        following_check=FollowerCount.objects.filter(user=user,Follower=follower).first()
        if following_check == None:
             FollowerCount.objects.create(user=user,Follower=follower)
        else:
            following_check.delete()
        return  redirect(f'profile/{user}') 
    



@login_required(login_url='signin')
def LikePost(request):
     
    post_id=request.GET['post']
    username=request.user
    Like_count=Like_Post.objects.filter(post_id=post_id,username=username).first()
    print("it's Not save at")
    if Like_count == None:
        like_posts=POST.objects.get(id=post_id)
        like_posts.like_count=like_posts.like_count+1
        print(like_posts.like_count)
        like_posts.save()
        Like_Post.objects.create(post_id=post_id,username=username)
         
         
    else:
        Like_count.delete()
        like_posts=POST.objects.get(id=post_id)
        like_posts.like_count=like_posts.like_count-1
        like_posts.save()
    return redirect('/')