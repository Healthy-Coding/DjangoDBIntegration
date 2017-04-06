from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Enter Subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'Enter Message'}))

    sender = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Enter Email'}))
