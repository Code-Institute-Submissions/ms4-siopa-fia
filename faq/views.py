from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Faq
from .forms import FaqForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def faq(request):
    """ a view to return the faqs page """
    faq = Faq.objects.all()

    context = {
        'faq': faq
    }

    return render(request, 'faq/faq.html', context)

@login_required
def add_faq(request):
    """ Add a blog post to the blog """

    if not request.user.is_superuser:
        messages.error(request, 'Only our siopaFIA team can access this.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FaqForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ Successfully Added!')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request, 'Failed to add FAQ. Please check the form is valid.')
    else:
        form = FaqForm()

    template = 'faq/add_faq.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_faq(request, faq_id):
    """a view to edit the faq"""
    if not request.user.is_superuser:
        messages.error(request, 'Only our siopaFIA team can access this.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            messages.success(request, 'FAQ successfully updated!')
            return redirect(reverse('faq'))
        else:
            messages.error(
                request, 'Unable to update faq. Please check your form.')
    form = FaqForm(instance=faq)
    messages.info(request, f'You are editing {faq.question}')

    template = 'faq/edit_faq.html'
    context = {
        'form': form,
        'faq': faq,
    }

    return render(request, template, context)


@login_required
def delete_faq(request, faq_id):
    """ Delete a faq """
    if not request.user.is_superuser:
        messages.error(request, 'Only our siopaFIA team are permitted to do this.')
        return redirect(reverse('home'))

    faq = get_object_or_404(Faq, pk=faq_id)
    faq.delete()
    messages.success(request, 'FAQ Successfully Deleted!')
    return redirect(reverse('faq'))
