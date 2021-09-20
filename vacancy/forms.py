from django import forms


class VacancyForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)
