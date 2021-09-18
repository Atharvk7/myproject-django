from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
   path("",views.indexa, name='home'),
   path("about",views.about, name='about'),
   path("services",views.services, name='services'),
   path("indexa",views.indexa,name="indexa"),
   path("contact",views.contact,name="contact")
   
]
'''
urlpatterns = [
    path('admin/', admin.site.urls),
]''' 