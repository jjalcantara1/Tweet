from django.shortcuts import render
from .forms import ContactForm


# Create your views here.

def home_page(request):
    return render(request, 'home.html', {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'form': contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, 'contact/contact.html', context)
