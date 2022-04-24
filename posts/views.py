from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, CreateView
from .models import Post
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

def Create(request):
    if request.method=='POST':
        blogforms = PostForm(request.POST)

        if blogforms.is_valid():
            blogforms.instance.user = request.user
            blogforms.save()
            return redirect('blogs')
    else:
        blogforms = PostForm()
        return render(request, 'posts/create.html', {'blogform':blogforms})



def blogs(request):
    blogs = Post.objects.all()
    paginator = Paginator(blogs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {'blogs':blogs, 'page_obj': page_obj}
    return render(request,'blogs.html',data)

def blog_details(request,slug):
    blog = Post.objects.get(slug=slug)
    data = {'blog':blog}
    return render(request,'blog-details.html',data) 


def dashblog_details(request,slug):
    blog = Post.objects.get(slug=slug)
    data = {'blog':blog}
    return render(request,'posts/dashview.html',data) 

@login_required
def update(request, slug):
    context = {}
    
    obj = get_object_or_404(Post, slug=slug, user__id=request.user.id)
    

    form = PostForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect("blogs")

    context["form"] = form

    return render(request, "posts/update.html", context)


def delete(request, slug):

    context = {}

    obj = get_object_or_404(Post, slug=slug)

    if request.method == "POST":
        obj.delete()

        return redirect("blogs")

    return render(request, "posts/delete.html", context)

def search(request):
    blogs = Post.objects.all()
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            blogs = blogs.filter(title__icontains=keyword)
        data = {'blogs':blogs}
        return render(request,"posts/search.html",data)
    else:
        return HttpResponse("No results found")




    
