from django import forms
from .models import MyGoal


class MyGoalsForm(forms.ModelForm):

    class Meta:
        model = MyGoal
        fields = '__all__'
