from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.forms import CharField, Form, PasswordInput

class UserForm(Form):
    user_name=CharField(max_length=64,label="User name",)
    password = CharField(widget=PasswordInput(),label="password")


import json
with open('./hello/sample.json',
'r') as f:
  js=json.load(f)
with open('./hello/Data.json',"r") as f:
  data=json.load(f)

# Create your views here.
def index(request):
  return render(request,'hello/boot.html',{
"items":list(range(10))
  })


def display(request,course,chapter,lesson,source):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))

  src="https://voe.sx/e/"+source
  #title=data[name]['title']
  #chapter=data[name]['chapter']
  
  return render(request, 'hello/display.html',{
    "src":src,
    "title":lesson,
    "chapter":chapter,
    "course":course
  })

def courses(request):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))

  return render(request,'hello/courses.html',{
    "courses":js['courses'],
    #"base_url":"chapter"
  })

def chapters(request,chapter):
  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('login'))
    
  #courses=js['courses']
  for course in js['courses']:
    title=course['title']
    if title==chapter:
      chapters=course['chapters']
  #chapters=courses['chapters']
    
  return render(request,'hello/chapters1.html',{
    "chapters":chapters,
    "course_name":chapter
    #"base":"lesson"       
  })


def login_view(request):
  if request.method=="POST":
    form=UserForm(request.POST)
    if form.is_valid():
      user_name=form.cleaned_data['user_name']
      password=form.cleaned_data['password']
      user=authenticate(request,username=user_name,password=password)
      if user is not None:
        login(request,user)
        return HttpResponseRedirect(reverse('course'))
      else:
        return render(request,'login/login.html',{
          "message":"invalid credentials"
        })
    
  return render(request,'login/login.html',{'form':UserForm})

def logout_view(request):
  logout(request)
  return render(request,'login/login.html',{"message":"logged out","form":UserForm()})
  pass