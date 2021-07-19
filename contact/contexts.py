from .forms import NewsletterSubscribeForm


def newsletter_subscribe_form(request):
    newsletter_form = NewsletterSubscribeForm()

    context = {
        'newsletter_form': newsletter_form,
    }

    return context
