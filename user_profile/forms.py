from django import forms
from django.db import models
from django.db.models import fields
from .models import UserProfile

""" MODEL FORM- TO WORK WITH DB DATA """
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=['first_name','last_name','address','mobile','dob','about','user_img','email']
        
        def __init__(self, *args, **kwargs):
            super(UserProfileForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
 