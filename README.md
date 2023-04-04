# Developing Django on Repl.it

- Fork this template to get started
- Simply hit run to start the server
- The server will autoreload as needed. You don't need to restart the server manually.

## Add your first view

1. Create a file under `mysite` named `views.py` with the following contents:

```
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

2. Add a url pattern under `mysite/urls.py`. It should look like this:

```
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
```

![Screenshot 2023-04-04 at 6 23 11 PM](https://user-images.githubusercontent.com/82832791/229797750-ed10e082-9502-4597-923b-1c8d17ce4d1a.png)
![Screenshot 2023-04-04 at 6 23 30 PM](https://user-images.githubusercontent.com/82832791/229797835-2ee3d25f-19fb-4f58-97f0-ad5d6ce46a4e.png)
![Screenshot 2023-04-04 at 6 24 00 PM](https://user-images.githubusercontent.com/82832791/229797971-1ae775a3-ef07-46f0-bf9d-f10574acfc66.png)
![Screenshot 2023-04-04 at 6 24 54 PM](https://user-images.githubusercontent.com/82832791/229798200-041c8cb6-0e4c-479b-80af-010027ab5bb7.png)
![Screenshot 2023-04-04 at 6 26 12 PM](https://user-images.githubusercontent.com/82832791/229798592-83dd060b-d1cb-4064-a03b-2a4a3be93bcd.png)


## Shell

Django utilizes the shell for managing your site. For this click on the `?` in the lower-right corner and click "Workspace shortcuts" from there you can open a new shell pane. 

## Database

By default this template utilizes the sqlite database engine. While this is fine for development it won't work with external users of your app as we don't persist changes to files when they happen outside the development environment. 

We suggest bringing a database using an outside service. 

See Django documentation on how to setup a database: https://docs.djangoproject.com/en/3.0/intro/tutorial02/

