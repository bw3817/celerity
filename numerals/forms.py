from django import forms


class NumeralsForm(forms.Form):
    some_number = forms.IntegerField(
        label='An integer',
        min_value=1,
        max_value=3999,
        required=True
    )
    roman_numerals = forms.CharField(label='Roman Numerals', required=False)
