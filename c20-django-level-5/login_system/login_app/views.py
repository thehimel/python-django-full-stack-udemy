from django.shortcuts import render
from login_app.forms import UserForm, UserProfileInfoForm

# Imports for authentication
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, 'login_app/index.html')


def register(request):
    registered = False

    if request.method == 'GET':
        user_form = UserForm()
        user_profile_info_form = UserProfileInfoForm()

    elif request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_profile_info_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile_info_form.is_valid():
            user = user_form.save()  # By defailt commit=True
            user.set_password(user.password)  # Hashing the password
            user.save()

            # Holding the commit to manipulate the data
            profile = user_profile_info_form.save(commit=False)
            profile.user = user  # Getting the user for one to one relationship

            # request.FILES is a dictionary that contains the files sent by the user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()  # Finally, saving with commit=True
            registered = True

        # Else data is invalid
        # else:
        #     print("User registration failed.")
        #     print(user_form.errors(), user_profile_info_form.errors())

    dictionary = {
        'registered': registered,
        'user_form': user_form,
        'user_profile_info_form': user_profile_info_form
    }

    # In this way, if user already exists, it renders the form showing the error.
    return render(request, 'login_app/register.html', context=dictionary)


def user_login(request):
    if request.method == 'GET':
        dictionary = {}
        return render(request, 'login_app/login.html', dictionary)

    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account not active.")

        else:
            print("Incorrect username and password!")
            print(f"Username: {username} and Password: {password}")
            return HttpResponse("Invalid login details.")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# An example view that requries login
@login_required
def profile(request):
    return HttpResponse("Login successful!")
