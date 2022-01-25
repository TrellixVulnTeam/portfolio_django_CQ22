from django.shortcuts import render
from .models import Resume, Post
#from django.views.generic import ListView
#from django import request
#from django.http import HttpResponse
#from .models import Resume , Post

# Create your views here.

def index(request):
    return render(request, 'resume/index.html')


def about(request):
    resume = Resume.objects.get(pk=1)
    return render(request, 'resume/about.html',{"resume":resume})   


def blog(request):
    post_objects = Post.objects.all().order_by('-date')
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        post_objects = post_objects.filter(title__icontains=item_name)
    return render(request, 'resume/blog.html', {'post_objects': post_objects})

    
def contact(request):
    return render(request, 'resume/contact.html')
    

def portfolio(request):
    return render(request, 'resume/portfolio.html')

#class PostListView(ListView):
#    model = Post
#    template_name = 'resume/blog.html'
#    context_object_name = 'post'
#
#    ordering = ['-date']

    