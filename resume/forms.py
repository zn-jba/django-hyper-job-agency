from django import forms


class ResumeForm(forms.Form):
    description = forms.CharField(label="Description", max_length=1024)
