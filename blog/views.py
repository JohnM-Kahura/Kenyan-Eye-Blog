from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import WriteForm


def discover_view(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }

    return render(request, 'Blog/discover.html', context)


def blog_details_view(request, pk):
    blog = Blog.objects.get(id=pk)

    context = {
        "blog": blog
    }
    return render(request, 'MVP/details.html', context)
# @login_required


def landing_page(request):
    blogs = Blog.objects.all()
    context = {
        "blogs": blogs
    }
    return render(request, 'MVP/home.html', context)


def write_view(request):
    form = WriteForm()
    if request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')

    context = {
        'form': form
    }

    return render(request, 'blog/write.html', context)


def update_blog_view(request,pk):

    blog=Blog.objects.get(id=pk)
    form=WriteForm(instance=blog)
    if request.method =='POST':
        form=WriteForm(request.POST,instance=blog)
        if form.is_valid:
            form.save()
            return redirect('landing_page')


    context={
        'form':form,
        'blog':blog,
    }        
    return render(request,'Blog/update.html',context)

def delete_blog_view(request,pk):
   
    blog=Blog.objects.get(id=pk)

    blog.delete()
    

    return redirect('landing_page')