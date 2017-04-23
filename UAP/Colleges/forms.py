from django import forms
import sys


PAGINATE = (
    (10, 10),
    (50, 50)
)

COLLEGE_SIZE = (
    (-1, 'Choose one...'),
    ((0, 999), '0-999 Students'),
    ((1000, 4999), '1000-4999 Students'),
    ((5000, 14999), '5000-14999 Students'),
    ((15000, sys.maxsize), '15000+ Students')
)

class SimpleSearchForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={
                            'class': 'form-control', 'placeholder': 'Search for Colleges'}))
    paginate_by = forms.ChoiceField(choices=PAGINATE, widget=forms.Select(attrs={'class': 'form-control'}))
    college_size = forms.ChoiceField(choices=COLLEGE_SIZE, widget=forms.Select(attrs={'class': 'form-control'}))
