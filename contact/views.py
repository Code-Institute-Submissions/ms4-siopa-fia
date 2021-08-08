from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.mail import send_mail

from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string, get_template

from .models import NewsletterSubscribe
from .forms import NewsletterSubscribeForm, ContactForm


def contact(request):
    """ a view to access contact page/form """
    template = 'contact/contact.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for your enquiry. \
                             We will get back to you as soon as possible!")

            instance = form.save()
            """Send email confirming message received"""
            sender_email = instance.email
            subject = render_to_string(
                'contact/confirmation_emails/message_received_subject.txt',
                {'instance': instance})
            body = render_to_string(
                'contact/confirmation_emails/message_received_body.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [sender_email],
            )

        else:
            messages.error(request, 'Message not sent.'
                           ' Please ensure the form is valid.')

    form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, template, context)

# subscribe to newsletter


def newsletter_signup(request):

    newsletter_form = NewsletterSubscribeForm(request.POST or None)
    template = 'contact/confirmation_emails/newsletter_subscribe_confirm_body.html'
    context = {
        'newsletter_form': newsletter_form,
    }

    if newsletter_form.is_valid():
        instance = newsletter_form.save(commit=False)
        if NewsletterSubscribe.objects.filter(email=instance.email).exists():
            messages.error(request, 'Oops! '
                           'This email already exists in our mailing list!')
        else:
            instance.save()
            messages.success(request, 'Woohoo! '
                             'You are now part of the siopaFIA community!')
            sender_email = instance.email
            subject = 'Thank You for Signing Up!'
            body = render_to_string(
                'contact/confirmation_emails/newsletter_subscribe_confirm_body.txt',
                {'instance': instance})
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [sender_email],
            )

    else:
        messages.error(request, 'Message not sent.'
                       ' Please ensure email is valid.')

    return render(request, template, context)


# To unsubscribe:

def newsletter_unsubscribe(request):
    newsletter_form = NewsletterSubscribeForm(request.POST or None)

    if newsletter_form.is_valid():
        instance = newsletter_form.save(commit=False)
        if NewsletterSubscribe.objects.filter(email=instance.email).exists():
            registered_email = [instance.email]
            subject = render_to_string(
                'contact/confirmation_emails/newsletter_unsubscribe_email_subject.txt'
            )
            body = render_to_string(
                'contact/confirmation_emails/newsletter_unsubscribe_email_body.txt',
                {'instance': instance,
                 'contact_email': settings.DEFAULT_FROM_EMAIL}
            )
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                registered_email,
            )
            NewsletterSubscribe.objects.filter(
                                               email=instance.email).delete()
            messages.success(request, f'{instance.email} \
                             has been removed from our mailing list')                               
        else:
            messages.error(request, 'Sorry! This email \
                           is not currently in our mailing list.')

    newsletter_form = NewsletterSubscribeForm()
    template = 'contact/confirmation_emails/newsletter_unsubscribe_confirm.html'
    context = {
        'newsletter_form': newsletter_form,
    }
    return render(request, template, context)
