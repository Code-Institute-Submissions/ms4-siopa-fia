from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail

from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string


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
            messages.error(request, 'Message failed to send.'
                           ' Please ensure the form is valid.')

    form = ContactForm()

    context = {
        'form': form,
    }

    return render(request, template, context)
