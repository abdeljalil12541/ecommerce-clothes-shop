from email.headerregistry import Address
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ProductReview, UserAddressBook

class SignUpForm(UserCreationForm):
    class Meta:
        model  = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')




# Review Add Form
class ReviewAdd(forms.ModelForm):

    class Meta:
        model  = ProductReview
        fields = ('review_text', 'review_rating')




# AddressBook Add Form 
class AddressBookAdd(forms.ModelForm):

    class Meta:
        model  = UserAddressBook
        fields = ('address', 'mobile', 'status')







# ProfileEdit Form 
class ProfileForm(UserChangeForm):

    class Meta:
        model  = User
        fields = ('first_name', 'last_name', 'email', 'username')