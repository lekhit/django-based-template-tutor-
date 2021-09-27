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
def display(request,name):

  src="https://voe.sx/e/"+name
  #title=data[name]['title']
  #chapter=data[name]['chapter']
  
  return render(request, 'hello/display.html',{
    "src":src,
    #"title":title,
    #"chapter":chapter
  })

def courses(request):
  lt=[]
  courses=dict()
  for course in js['courses']:
    #courses[course['id']]=course['title']
    lt.append([int(course['id']),course['title']])
     
    print(courses)
  return render(request,'hello/courses.html',{
    "courses":js['courses'],
    "base":"chapter"
  })

def chapters(request,code):

  courses=js['courses'][code-1]
  for course in js['courses']:
    title=course['title']
    chapters=course['chapters']
  chapters=courses['chapters']
    
  return render(request,'hello/chapters1.html',{
    "chapters":chapters,
    "base":"lesson"       
  })