from django.shortcuts import render


def about(request):
    """ A view to return the about us page """
    return render(request, 'about/about.html')
