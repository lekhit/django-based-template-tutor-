from django.urls import path
from . import views
urlpatterns=[
  path('',views.index,name='index'),
  path('courses',views.courses,name='courses'),
  path('ch',views.chapters,name='chapters'),
  path('<str:name>',views.display,name='display'),
  ]