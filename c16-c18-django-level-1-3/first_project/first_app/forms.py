from django import forms
from django.core import validators
from first_app.models import UserDetails


# Simple form
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)


# Individual Validator
def check_for_alphabet(value):
    if not value.isalpha():
        raise forms.ValidationError("Name can be alphabet only.")


# Form to illustrate validators in Django
class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, validators=[check_for_alphabet])
    email = forms.EmailField(max_length=100)
    verify_email = forms.EmailField(max_length=100, label="Repeat Email:")
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    """
    Bot Catcher: A hidden field with condition max_length = 0.
    If a bot fills the form, it will fill this hidden field also.
    If the length of this field is more than 0, then it's a bot.
    """
    botcatcher = forms.CharField(
        required=False,
        widget=forms.HiddenInput,
        validators=[validators.MaxLengthValidator(0)],
    )

    """
    This function cleans all the data and we put some validator code here,
    so that when it runs, it also checks for these conditions. This is used
    for bulk validation checks.
    """

    def clean(self):
        all_clean_data = super().clean()

        email = all_clean_data["email"]
        verify_email = all_clean_data["verify_email"]

        if email != verify_email:
            raise forms.ValidationError("Emails must match.")


# Form to illustrate Models Form in Django
"""Creating a form according to the model."""


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = "__all__"
        # fields = ["first_name", "last_name", "email"]
        # exclude = ["last_name", "email"]
