from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/',homepage,name='homepage'),
    path('',base,name='base'),
    path('addmenu/',addmenu,name='addmenu'),
    path('addchef/',addchef,name='addchef'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('menu/',menu,name='menu'),
    path('event/',event,name='event'),
    path('chef/',chef,name='chef'),
    path('dashboard/',dashboard,name='dashboard'),
    path('delete/<int:id>',delete,name='delete'),
    path('deletemenu/<int:id>',deletemenu,name='deletemenu'),
    path('edit/<int:id>',edit,name='edit'),
    path('editmenu/<int:id>',editmenu,name='editmenu'),
    path('update/',update,name='update'),
    path('home/',home,name='home'),
    path('updatemenu/',updatemenu,name='updatemenu'),
    path('loginpage/',loginpage,name='loginpage'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('registerpage/', registerpage,name='registerpage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
