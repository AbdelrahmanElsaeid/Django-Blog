from django.shortcuts import render
from .models import Post
# Create your views here.



def posts_list(request):
    all = Post.objects.all()
    return render(request,'all_posts.html',{'data':all})

def posts_detail(request,post_id):
    single = Post.objects.get(id = post_id)
    return render(request, 'detail.html', {'data':single})    