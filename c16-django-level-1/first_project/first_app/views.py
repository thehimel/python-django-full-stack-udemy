from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
from first_app import forms

def index(request):
    my_dictionary = {
        "subject":  "Trees in the Forest.",
    }

    return render(request, 'first_app/index.html', context=my_dictionary)


def access_records(request):
    access_records_list = AccessRecord.objects.order_by('date')

    access_records_dictionary = {
        'access_records': access_records_list
    }

    return render(request, 'first_app/access_records.html', context=access_records_dictionary)


def contact_form_view(request):
    # If POST Request is received
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)

        if form.is_valid():
            print("Form validation successful!")
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")
            print(f"Text: {form.cleaned_data['text']}")

            message = "Thanks for contacting us. We'll get back to you soon."

        else:
            message = "Sorry! Something is wrong. Try again lager."

        # Render the contact page with the message
        return render(request, 'first_app/contact.html', {'message': message})

    # Render the form
    else:
        contact_form = forms.ContactForm()
        return render(request, 'first_app/contact.html', {'contact_form': contact_form})

