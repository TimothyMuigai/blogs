from django.urls import path
from . import views
from django.urls import path
from blogApp.views import login_view

urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('blogs/',views.display_blogs, name='display_blogs'),
    path('subscribe/',views.subscribe, name='subscribe'),
    path('create_blog/',views.create_blog, name='create_blog'),
    path('delete/<int:blogID>/',views.delete_blog, name='delete_blog'),
    path('edit/<int:pk>', views.edit_blog, name='edit_blog'),
    path('cancel/', views.cancel_action, name='cancel_action'),    
    path('accounts/register/', views.register, name='register'),
    path('login/', login_view, name='login'),
]