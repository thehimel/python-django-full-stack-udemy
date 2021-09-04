from django.shortcuts import render

# from django.http import HttpResponse
# from first_app.models import Topic, Webpage, UserDetails
from first_app.models import AccessRecord, UserDetails
from first_app import forms


def index(request):
    my_dictionary = {
        "subject": "Trees in the Forest.",
    }

    return render(request, "first_app/index.html", context=my_dictionary)


def access_records(request):
    access_records_list = AccessRecord.objects.order_by("date")

    access_records_dictionary = {"access_records": access_records_list}

    return render(
        request, "first_app/access_records.html", context=access_records_dictionary
    )


# Simple form
def contact_form_view(request):
    # Render the form
    if request.method == "GET":
        form = forms.ContactForm()
        return render(request, "first_app/form.html", {"form": form})

    # If POST Request is received
    elif request.method == "POST":
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
        return render(request, "first_app/form.html", {"message": message})


# Form to illustrate validators in Django
def registration_form(request):
    # Render the form
    if request.method == "GET":
        form = forms.RegistrationForm()
        return render(request, "first_app/form.html", {"form": form})

    # If POST Request is received
    elif request.method == "POST":
        form = forms.RegistrationForm(request.POST)

        if form.is_valid():
            print("Form validation successful!")
            print(f"Name: {form.cleaned_data['name']}")
            print(f"Email: {form.cleaned_data['email']}")

            # Render the registration page with the message
            message = "Registration successful!"
            return render(request, "first_app/form.html", {"message": message})

        else:
            return render(request, "first_app/form.html", {"form": form})


# Signup a new user
def user_signup_form(request):
    if request.method == "GET":
        form = forms.UserSignupForm()
        return render(request, "first_app/form.html", {"form": form})

    elif request.method == "POST":
        form = forms.UserSignupForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)  # Redirect to index after successfull signup

        else:
            message = "Sorry! Something is wrong. Try again lager."
            return render(request, "first_app/form.html", {"message": message})


# Show the list of users
def users(request):
    user_list = UserDetails.objects.order_by("first_name")
    dictionary = {"users": user_list}
    return render(request, "first_app/users.html", context=dictionary)
