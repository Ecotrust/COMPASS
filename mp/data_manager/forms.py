from django import forms


class UploadContentsForm(forms.Form):
    file = forms.FileField()
