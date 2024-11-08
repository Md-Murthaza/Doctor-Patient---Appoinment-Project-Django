from django import forms
from .models import Appoinment
from django.forms import ModelForm


class AppoinmentForm(ModelForm):
    class Meta:
        model = Appoinment
        fields = ['doctor','appoinments_time']


    def clean_appoinments_time(self):
        appoinments_time = self.cleaned_data['appoinments_time']
        if appoinments_time < timezone.now():
            raise forms.ValidationError("Appoinment time cannot be in the past")
        return appoinments_time