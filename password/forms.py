from django import forms
from .models import Generate

class GenerateForm(forms.ModelForm):
    class Meta:
        model = Generate
        fields = ('scale', 'special', 'simple', 'password', 'passphrase')
        labels = {
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
                'oninput': 'checkPasswordStrength()',
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
                'oninput': 'checkPasswordStrength()'
            })
        }
