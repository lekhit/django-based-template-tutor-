from django.db import models

# Create your models here.




class Course(models.Model):
  title=models.CharField(max_length=256)

  def __str__(self):
    return f'{self.title} (id:{self.id}) '

class Chapter (models.Model):
  title=models.CharField(max_length=256)
  index=models.FloatField()
  course=models.ForeignKey(Course, on_delete=models.CASCADE,related_name="chapters")


  def __str__(self):
    return f'{self.course} / {self.title} (id:{self.id}, index:{self.index}) '
default=''
class Lesson (models.Model):
  title=models.CharField(max_length=256)
  index=models.FloatField()
  chapter=models.ForeignKey(Chapter, on_delete=models.CASCADE,related_name="lessons")
  course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')

  def __str__(self):
    return f'{self.chapter} / {self.title} (id:{self.id}, index:{self.index}) '

class Source (models.Model):
  voe=models.CharField(max_length=256)
  lesson= models.ForeignKey(Lesson, on_delete=models.CASCADE,related_name="source")

  def __str__(self):

    return f'{self.lesson} / {self.voe} (id:{self.id}) '

"""
s=Source.objects.create(
  voe="source",
  lesson=Lesson.objects.get_or_create(
    title="lesson_title",
    chapter=Chapter.objects.get_or_create(
      title='chapter_title',
      course=Course.objects.get_or_create(
        title="course_title"
      )[0]
    )[0]
  )[0]
)

s=Source.objects.create(
  voe=item['source'],
  lesson=Lesson.objects.get_or_create(
    title=item.get("title"),
    course=Course.objects.get_or_create(
        title=item.get("course")
      )[0],
    index=num(item.get('title'))
    chapter=Chapter.objects.get_or_create(
      title=item.get('chapter'),
      index=num(item.get('chapter')),
      course=Course.objects.get_or_create(
        title=item.get("course")
      )[0]
    )[0]
  )[0]
)

import re
pat=re.compile(r'\d{1,}')
def num(item,default=0):
  rs=pat.search(item) 
  if rs:
    return float(rs[0])
  else:
    print(item,'no index found so returned 0')
    return default
path=''
with open(path,'r') as f:
  js=json.load(f)
for i,item in enumerate(js['data']):
      s=Source.objects.create(
    voe=item['source'],
    lesson=Lesson.objects.get_or_create(
      title=item.get("title"),
      course=Course.objects.get_or_create(
          title=item.get("course")
        )[0],
      index=num(item.get('title'),i),
      chapter=Chapter.objects.get_or_create(
        title=item.get('chapter'),
        index=num(item.get('chapter'),i),
        course=Course.objects.get_or_create(
          title=item.get("course")
        )[0]
      )[0]
    )[0]
  )

from hello.models import *
import re,json
pat=re.compile(r'\d{1,}')
def num(item,default=0):
  rs=pat.search(item) 
  if rs:
    return float(rs[0])
  else:
    print(item,'no index found so returned 0')
    return default

class update:
  def update_one(self,item,i):
    s=Source.objects.create(
          voe=item['source'],
          lesson=Lesson.objects.get_or_create(
            title=item.get("title"),
            course=Course.objects.get_or_create(
                title=item.get("course")
              )[0],
            index=num(item.get('title'),i),


            chapter=Chapter.objects.get_or_create(
              title=item.get('chapter'),
              index=num(item.get('chapter'),i),

              
              course=Course.objects.get_or_create(
                title=item.get("course")
              )[0]
            )[0]
          )[0]
        )
  def __init__(self,address=None):
    if address:
      self.put_data(address)
  def put_data(self,address):
    with open(address,'r') as f:
      i=0
      for item in json.load(f)['data']:
            i+=1
            self.update_one(item,i)

put_data('hello/data.json')

"""