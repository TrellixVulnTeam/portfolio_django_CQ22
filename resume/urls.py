from django.urls import path
from . import views
#from . views import PostListView


app_name = 'resume'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),   
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'), 
]
