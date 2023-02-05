from django.shortcuts import render
from django.views.generic import ListView, DetailView
from posts.models import Post
from django.views.generic.edit import UpdateView, DeleteView, CreateView

# Create your views here.


class PostList(ListView):
    model = Post
    # template : post_list.html    (By Default)
    # context : object_list    or    post_list  (By Default)


class PostDetail(DetailView):
    model = Post    
    # template : post_detail.html    (By Default)
    # context : object    or    post    (By Default)

class PostCreate(CreateView):
    model = Post
    fields = {'title','content', 'tags', 'image', 'author'}
    success_url = '/blog'    


class PostUpdate(UpdateView):
    model = Post
    fields = {'title','content', 'tags', 'image', 'author'}
    success_url = '/blog'        

class PostDelete(DeleteView):
    model = Post
    success_url = '/blog'    
