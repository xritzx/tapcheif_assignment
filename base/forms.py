from django import forms

class TextForm(forms.Form):
    text = forms.CharField(max_length=1000000000, required=False, widget=forms.Textarea)
