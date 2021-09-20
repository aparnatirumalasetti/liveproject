from . import views
from django.urls import path
urlpatterns = [
path('website/', views.website,name='website'),
path('register/', views.registration,name='register'),
path('library/', views.library,name='library'),
path('contact/', views.contact,name='contact'),
path('about/', views.about,name='about'),
path('administration/', views.administration,name='administration'),
]

'''path('website/register/', views.registration,name='register'),
path('website/contact/', views.contact,name='contact'),
path('website/administration/', views.administration,name='administration'),
path('website/about/', views.about,name='about'),
path('website/library/', views.library,name='library'),


path('contact/library/', views.library,name='library'),
path('contact/register/', views.register,name='register'),
path('contact/about/', views.about,name='about'),
path('contact/administration/', views.administration,name='administration'),
path('contact/website/', views.website,name='website'),

path('about/website/', views.website,name='website'),
path('about/register/', views.register,name='register'),
path('about/administration/', views.administration,name='administration'),
path('about/contact/', views.contact,name='contact'),
path('about/library/', views.library,name='library'),


path('administration/website/', views.website,name='website'),
path('administration/library/', views.library,name='library'),
path('administration/about/', views.about,name='about'),
path('administration/contact/', views.contact,name='contact'),
path('administration/register/', views.register,name='register'),

path('register/website/', views.website,name='website'),
path('register/library/', views.library,name='library'),
path('register/about/', views.about,name='about'),
path('register/contact/', views.contact,name='contact'),
path('register/administration/', views.administration,name='administration'),
'''
