from django import forms


class CreateRockForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.TextField()
    slug = forms.CharField(max_length=255)