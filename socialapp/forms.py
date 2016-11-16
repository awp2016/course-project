from django import forms


class StatusForm(forms.Form):
    text = forms.CharField(label="Status", widget=forms.Textarea)
