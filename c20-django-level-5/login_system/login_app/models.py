from django.db import models
from django.contrib.auth.models import User

# One to one relationship with the built-in model User adding some fields.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional
    portfolio_url = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


"""
Note for using models.ImageField():
Library for pictures:
pip install pillow
If you get any error like jpeg support disabled:
pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
"""
