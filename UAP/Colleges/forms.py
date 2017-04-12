from django import forms

PAGINATE = (
    (10, 10),
    (50, 50)
)


class SimpleSearchForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={
                            'class': 'form-control', 'placeholder': 'Search for Colleges'}))
    paginate_by = forms.ChoiceField(choices=PAGINATE, widget=forms.Select(attrs={'class': 'dropdown-item'}))
