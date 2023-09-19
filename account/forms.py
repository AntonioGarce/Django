from django import forms
from django.core.exceptions import ValidationError


class UpdatePhotoForm(forms.Form):
    img = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'p-2',
                                                          'style': 'width: fit-content; display: block;'
                                                          }))


class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль...',
                                                                 'class': 'filter-input'}),
                               error_messages={'invalid': 'Вы не прошли капчу'})

    new_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль...',
                                                                 'class': 'filter-input'}),
                                   error_messages={'invalid': 'Вы не прошли капчу'})

    def clean_new_password(self):
        clean_new_password = self.cleaned_data('new_password')
        if self.cleaned_data('password') == clean_new_password:
            raise ValidationError('Пароли не должны совпадать!')
        return clean_new_password












