from django.shortcuts import render, redirect
from django.contrib import messages

from ..models import Blog, BlogCategory
from ..forms import NewCommentForm

def index(request):
    categories = BlogCategory.objects.all()
    blogs = Blog.objects.all()

    context = {
        'categories': categories,
        'blogs': blogs,
    }
    return render(request, 'blog/index.html', context)



def show(request, slug):
    blog = Blog.objects.get(slug = slug)
    form = NewCommentForm()

    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()

            return redirect('blog.show', blog.slug)
        else:
            messages.error(request, 'An error occured during commenting')

    context = {
        'blog': blog,
        'form' : form
    }

    return render(request, 'blog/show.html', context)



def category(request, slug):
    categories = BlogCategory.objects.all()
    category = BlogCategory.objects.get(slug= slug)
    blogs = Blog.objects.filter(category = category.id)

    context = {
        'category': category,
        'categories': categories,
        'blogs': blogs
    }

    return render(request, 'blog/index.html', context)