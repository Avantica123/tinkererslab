from django.shortcuts import render,HttpResponse,redirect
from .forms import Signupform,loginform,pachange,profilechangeform
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from .models import Blogpost,blogcomment,Event,Notification
from datetime import datetime,date,timedelta
from django.contrib.auth.decorators import login_required



# Create your views here.
def notify(request):
    notifications=Notification.objects.all().order_by('id').reverse()
    return render(request,"noti.html",{"notifications":notifications})

def events(request):
    events=Event.objects.all().order_by('id').reverse()
    return render(request,'event.html',{"events":events})

def about(request):
    return render(request,"about-us.html")

@login_required(login_url='login')
def deletepost(request):
    id=request.POST.get('deletedata')
    comment=blogcomment.objects.get(pk=id)
    comment.delete()
    messages.success(request,"Post Delete Successfully")
    return redirect('filter1')

@login_required(login_url='login')
def deletepost2(request):
    id=request.POST.get('deletedata')
    comment=blogcomment.objects.get(pk=id)
    comment.delete()
    messages.success(request,"Post Delete Successfully")
    return redirect('profile')
@login_required(login_url='login')
def filter1(request):
    comment=blogcomment.objects.filter(user=request.user).order_by('id').reverse()
    return render(request,'filter1.html',{"comment":comment})

@login_required(login_url='login')
def filter2(request):
    
    # comment=blogcomment.objects.filter(timestamp=today)
    today = date.today()
    comment =  blogcomment.objects.filter(timestamp__year=today.year,
                                       timestamp__month=today.month,
                                       timestamp__day=today.day).order_by('id').reverse()
    print(comment)
    return render(request,'filter2.html',{"comment":comment})

def index(request):
    return render(request,"index.html")

def signup(reqeust):
    if reqeust.method == "POST":
        form=Signupform(reqeust.POST)
        if form.is_valid():
            form.save()
            messages.success(reqeust,"You Have Register Successfully!!")
            return redirect('login')
    else:
        form=Signupform()
        
    return render(reqeust,"signup.html",{"form":form})


def loginuser(request):
    username=None
    if request.method=="POST":
        form=loginform(request=request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("/")
                
    else:
        form=loginform()
    return render(request,'login.html',{"form":form})

def signout(request):
    logout(request)
    return redirect('/')



# @login_required(login_url="login")
def forum(request):
    comment=blogcomment.objects.filter(parent=None).order_by('id').reverse()
    replies=blogcomment.objects.exclude(parent=None).order_by('id').reverse()
    replydict={}
    for reply in replies:
        if reply.parent.id not in replydict.keys():
            replydict[reply.parent.id]=[reply]
        else:
            replydict[reply.parent.id].append(reply)
        
        
    return render(request,"forum.html",{"comment":comment,"replydict":replydict})



def postcommentss(request):
        orderby=request.POST.get('orderby')
        print(orderby)
        comment=request.POST.get('comment')
        user=request.user
        parentSno=request.POST.get('parentSno')
        image=request.FILES.get('image')
        if parentSno=="":
            comment=blogcomment(comment=comment,image=image,user=user,timestamp=datetime.today())
            comment.save()
            messages.success(request,"Post Added Successfully")
        else:
            parent=blogcomment.objects.get(id=parentSno)
            comment=blogcomment(comment=comment, image=image,user=user,timestamp=datetime.today(),parent=parent)
            comment.save()
        
        return redirect ('forum')
        
@login_required(login_url='login')
def profile(request):
    comment=blogcomment.objects.filter(user=request.user).order_by('id').reverse()

    if request.method=="POST":
        form=pachange(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request," Update Successfully")
            return redirect('login')

    else:
        form=pachange(user=request.user)
       
    return render(request,'profile.html',{"form":form,"comment":comment})



      
     
    
    

 


