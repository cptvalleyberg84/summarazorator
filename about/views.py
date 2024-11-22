from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def about_srzr(request):

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS,
            "Collaboration request received! Thank you for interest. We will get back to you as soon as we can.")

    """
    Renders the About Summarazorator page
    """
    about = About.objects.all().order_by('-about_updated_on').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        'about/about.html',
        {
            'about': about,
            'collaborate_form': collaborate_form
        },
    )

