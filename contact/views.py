from django.shortcuts import (render, redirect, 
                              reverse)
from django.core.mail import send_mail, EmailMultiAlternatives

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

    if newsletter_form.is_valid():
        instance = newsletter_form.save(commit=False)
        if (NewsletterSubscribe.objects.filter
                (email=instance.email).exists()):
                NewsletterSubscribe.objects.filter(email=instance.email).delete()
                messages.error(request, 'Sorry, that email is already in our system.')
        else:
            instance.save()
            messages.success(request, 'Hurray! You have been added to our mailing list!')
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = [instance.email]
            subject = 'Thank You for Signing Up!'
            body = render_to_string(
                'contact/confirmation_emails/newsletter_subscribe_confirm_body.txt',
                {'instance': instance}
            )
            signup_confirmation_email = EmailMultiAlternatives(
                                    subject=subject,
                                    body=body,
                                    from_email=from_email,
                                    to=to_email)

            html_template = get_template(
                'contact/confirmation_emails/newsletter_signup_confirmation_body.html'
                ).render()
            signup_confirmation_email.attach_alternative(html_template,
                                                         'text/html')
            signup_confirmation_email.send()                       

    context = {
        'newsletter_form': newsletter_form,
    }
    template = 'contact/confirmation_emails/newsletter_subscribe_confirm_body.html'
    return render(request, template, context)

# To unsubscribe
def newsletter_unsubscribe(request):
    newsletter_form = NewsletterSubscribeForm(request.POST or None)

    if newsletter_form.is_valid():
        instance = newsletter_form.save(commit=False)
        if NewsletterSubscribe.objects.filter(email=instance.email).exists():
            NewsletterSubscribe.objects.filter(
                                               email=instance.email).delete()
        else:
            messages.error(request, 'Sorry! This email already exists.')

    context = {
        'newsletter_form': newsletter_form,
    }

    template = 'contact/newsletter_unsubscribe.html'
    return render(request, template, context)
