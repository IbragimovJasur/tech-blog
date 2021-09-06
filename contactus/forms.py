from django import forms
from .models import Message

class MessageCreateForm(forms.ModelForm):

    class Meta:
        model= Message  
        fields= ['name', 'email', 'phone', 'subject_of_message', 'content_of_message']
        widgets= {
            'name': 
            forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
                }),
                
            'email': 
            forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Email address'
                    }),

            'phone': 
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone'
                    }),

            'subject_of_message': 
            forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Subject'
                    }),

            'content_of_message': 
            forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Message'
                    }),
        }