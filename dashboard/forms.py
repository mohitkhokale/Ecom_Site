from django import forms
from dashboard.models import Dashboard


class dashboardForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = '__all__'


