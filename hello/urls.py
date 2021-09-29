from django.urls import path
from . import views
urlpatterns=[
  path('',views.index,name='index'),
  path('login/',views.login_view,name="login"),
  path('logout/',views.logout_view,name="logout"),
  
  path('course/',views.courses,name='course'),
  path('lesson/<str:chapter>',views.chapters,name='chapters'),
  path('<str:course>/<str:chapter>/<str:lesson>/<str:source>',views.display,name="display"),
  #path('<str:name>',views.display,name='display'),
  ]