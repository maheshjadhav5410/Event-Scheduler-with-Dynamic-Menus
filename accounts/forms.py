
from django import forms
from accounts.models import userDetails
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        # fields = '__all__'
        fields =['username','email','password']
        
class userProfileForm(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = ['phone','house_no','street','city','state','zipcode','profile_pic']
    captcha = ReCaptchaField()
    
class UpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','email']
        
class UserDetailsUpdateForm(forms.ModelForm):
    class Meta:
        model = userDetails
        fields = ['phone','house_no','street','city','state','zipcode','profile_pic']