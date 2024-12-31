from django import forms
from .models import TextTransformation

class TransformPhonetiqueForm(forms.ModelForm):

    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',      
            'placeholder': 'Entrez votre texte ici...',
            'rows': 5,                     
        })
    )

    delete_e = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',   
        })
    )

    delete_muet = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    delete_doublons = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    replace_s = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    replace_z = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    replace_o = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    replace_e = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    replace_en = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        })
    )

    class Meta:
        model = TextTransformation
        fields = (
            'text', 'delete_e', 'delete_muet', 'delete_doublons', 
            'replace_s', 'replace_z', 'replace_o', 'replace_e', 'replace_en'
        )
