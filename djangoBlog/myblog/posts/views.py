from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm
# Create your views here.



def posts_list(request):
    query = request.GET.get('q',None)
    all = Post.objects.all()
    if query is not None:
        all = all.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(slug__icontains=query)
        )
    return render(request,'all_posts.html',{'data':all})




def posts_detail(request,post_id):
    single = Post.objects.get(slug = post_id)
    return render(request, 'detail.html', {'data':single}) 



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
    else:
        form = PostForm()        
    return render(request,'new.html',{'x':form})    


def edit_post(request,post_id):   
    single = Post.objects.get(slug = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES,instance=single)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
    else:
        form = PostForm(instance=single)        
    return render(request,'edit.html',{'x':form})       


def delete_post(request, post_id):
    single = Post.objects.get(slug = post_id)
    single.delete()
    return redirect('/blog/')  

