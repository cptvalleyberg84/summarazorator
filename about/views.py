from django.shortcuts import render
from .models import About

# Create your views here.
def about_srzr(request):
    """
    Renders the About Summarazorator page
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        'about/about.html',
        {'about': about},
    )