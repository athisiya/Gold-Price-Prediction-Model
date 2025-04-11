from django import forms

class YearForm(forms.Form):
    year = forms.FloatField(label="Enter Year")
