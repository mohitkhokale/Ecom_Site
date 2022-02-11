from django import forms
from django.db import models
from django.db.models import fields
from .models import UserProfile

""" MODEL FORM- TO WORK WITH DB DATA """
class userupdateform(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # fields=['name','description']
