from django import forms
from .models import Lead, Agent, User
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import  UserCreationForm, UsernameField

User = get_user_model()

class LeadForm(forms.ModelForm):
    first_name=  forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'first_name'}))
    last_name=  forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'last_name'}))
    age=  forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'age'}))
    first_name=  forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'first_name'}))
    agent = forms.ModelChoiceField(queryset=Agent.objects.all(
    ), required=True, widget=forms.Select(attrs={'class': 'form-control agent', 'id': 'agent'}))
    class Meta:
        model = Lead
        fields = ('__all__')
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}