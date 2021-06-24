from django.shortcuts import render

from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IyDEFH3S6LmgNT4hbklLNXGxopw1HPywwtYvagtRzBOonkeBzlV8XTHHxVaxK22ekNy40UoQVNWAFAlNGX88tTQ00E8l3WzEu',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
