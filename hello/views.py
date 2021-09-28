from django.shortcuts import render
from django.http import HttpResponse
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

  return render(request,'hello/courses.html',{
    "courses":js['courses'],
    #"base_url":"chapter"
  })

def chapters(request,chapter):

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