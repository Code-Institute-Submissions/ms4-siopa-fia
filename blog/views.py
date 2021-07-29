from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required


def blog(request):
    """ A view to display all blogs """
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """A view to show individual blog post"""
    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
        }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    """ Add a blog post to the blog """

    if not request.user.is_superuser:
        messages.error(request, 'Only our siopaFIA team can access this.')
        return redirect(reverse('homepage'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Blog Successfully Added!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add the blog post. \
                           Please check the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    """ Edit a blog"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only siopaFIA admin can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, f'Successfully updated {blog.title}!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, f'Failed to update {blog.title}.\
                                     Please check the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


@login_required
def delete_blog(request, blog_id):
    """ Delete Blog """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only siopaFIA admin can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    messages.success(request, 'Blog Successfully Deleted!')
    return redirect(reverse('blog'))
