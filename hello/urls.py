from django.urls import path
from . import views
urlpatterns=[
  path('',views.index,name='index'),
  path('login/',views.login_view,name="login"),
  path('logout/',views.logout_view,name="logout"),
  
  path('course/',views.courses1,name='course'),
   path('lesson/<int:course_id>',views.chapters1,name='chapters'),
  path('lesson/<str:chapter>',views.chapters,name='chapters'),
   path('display/<int:lesson_id>',views.display1,name="display"),
	path('display/<str:source>/<int:lesson_id>',views.custom_display,name="custom_display"),
  path('<str:course>/<str:chapter>/<str:lesson>/<str:source>',views.display,name="display"),
  #path('<str:name>',views.display,name='display'),
  ]