from django.shortcuts import render

from .models import Blog

def blog(request):
    """ A view to display blogs """
    blog = Blog.objects.all()

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog.html', context)
