from django import forms

class PostSearchForm(forms.Form):
    query = forms.CharField(label='Filter', required=False)

    def filter_queryset(self, request, queryset):
        if self.cleaned_data['title']:
            return queryset.filter(title__icontains=self.cleaned_data['query'])
        return queryset

