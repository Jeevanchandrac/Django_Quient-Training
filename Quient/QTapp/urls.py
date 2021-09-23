from django.contrib import admin
from django.urls import path
from QTapp import views

#This is path for View.py

urlpatterns = [
   path('', views.home,name='home'),
   path('about', views.about,name='about'),
   path('Testimonials', views.Testimonials,name='Testimonials'),
   path('Gallery', views.Gallery,name='Gallery'),
   path('contact', views.contact,name='contact'),
   path('Viewdb', views.Viewdb,name="Viewdb"),
   path('delete/<int:id>/',views.delete_data,name='deletedate'),
   path('search_contacts', views.search_contacts,name="search_contacts")
]
