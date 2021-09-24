from django.urls import path
from . import views
urlpatterns=[
  path('',views.index,name='index'),
  path('ch',views.chapters,name='chapters'),
  path('<str:name>',views.display,name='display'),
  ]