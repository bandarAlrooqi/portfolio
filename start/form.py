from django.forms import ModelForm
from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    name = forms.CharField(max_length=255,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'type': 'email'}))
    subject = forms.CharField(max_length=255,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}))

    class Meta:
        model = Message
        fields = '__all__'
