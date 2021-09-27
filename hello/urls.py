from django.urls import path
from . import views
urlpatterns=[
  path('',views.index,name='index'),
  path('course',views.courses,name='course'),
  path('chapter/<str:name>',views.chapters,name='chapters'),
  path('lesson/<str:name>',views.display,name="display"),
  #path('<str:name>',views.display,name='display'),
  ]