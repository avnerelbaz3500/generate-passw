from django import forms

from .models import Generate

import string

CHOICES = [(str(separator), f"{separator}") for separator in string.punctuation]

class GenerateForm(forms.ModelForm):
    separator = forms.ChoiceField(choices=CHOICES, required=False, widget=forms.Select(attrs={
        'id': 'separator',
        'class': 'form-select w-25 mx-auto text-center '
    }))
    class Meta:
        model = Generate
        fields = ('scale', 'special', 'simple', 'password', 'passphrase','dico_scale','separator')
        labels = {
            'separator' : 'Choix du séparateur',
            'dicoscale' : 'Choix du nombre de mots',
            'scale': 'Taille du mot de passe',
            'special': 'Caractères spéciaux',
            'simple': 'Mot de passe simple',
            'password': 'Vérificateur de Mot de Passe',
            'passphrase': 'Mot de passe créé à partir d\'une phrase'
        }
        widgets = {
            'scale': forms.NumberInput(attrs={
                'id': 'scale',
                'class': 'form-range',
                'type': 'range',
                'step': '1',
                'min': '5',
                'max': '20',
                'oninput': 'classicalPassword()',
                'value': '8'
            }),
            'special': forms.CheckboxInput(attrs={
                'id': 'special',
                'class': 'form-check form-check-inline'
            }),
            'simple': forms.CheckboxInput(attrs={
                'id': 'simple',
                'class': 'form-check form-check-inline'
            }),
            'password': forms.TextInput(attrs={
                'id': 'password',
                'class': 'form-control',
                'placeholder': 'Testez votre mot de passe ici.',
                'oninput': 'checkPasswordStrength()'
            }),
            'passphrase': forms.TextInput(attrs={
                'id': 'passphrase',
                'class': 'form-control',
                'placeholder': 'Génèrer un mot de passe à partir d\'une phrase.',
                'oninput': 'passPhrase()'
            })
            ,'dico_scale': forms.NumberInput(attrs={
                'id': 'dico_scale',
                'class': 'form-range',
                'type': 'range',
                'step': '1',
                'min': '2',
                'max': '6',
                'oninput': 'dicoPassword()',
                'value': '4'
            }),

        }
