from django import forms


class StatusForm(forms.Form):
    text = forms.CharField(label="Status", widget=forms.Textarea)


class CommentForm(forms.Form):
    text = forms.CharField(label="Comment", widget=forms.Textarea)
