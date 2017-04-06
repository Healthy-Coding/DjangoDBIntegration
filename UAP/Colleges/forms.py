from django import forms


class SimpleSearchForm(forms.Form):
    query = forms.CharField(label='Filter', required=False)

    def filter_queryset(self, request, queryset):
        print("TESTING")
        print(self.cleaned_data)
        if self.cleaned_data['query']:
            return queryset.filter(university__icontains=self.cleaned_data['query'])
        return queryset
