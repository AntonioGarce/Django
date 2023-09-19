from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField, CaptchaTextInput, CaptchaAnswerInput
from django.core.exceptions import ValidationError


class CustomCaptchaTextInput(CaptchaTextInput):
    template_name = 'custom_field.html'


class CapForm(forms.Form):
    captcha = CaptchaField(required=False, widget=CustomCaptchaTextInput(attrs={'placeholder': 'Код с картинки', 'class': 'mt-3'}),
                           error_messages={'invalid': 'Вы не прошли капчу',
                                           'required': 'Вы не прошли капчу'})

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        if not captcha:
            raise ValidationError('Вы не прошли капчу')
        return captcha


class UserForm(forms.ModelForm):
    login = forms.CharField(max_length=150, required=False, label='Юзернейм', widget=forms.TextInput(attrs={'placeholder': 'Логин', 'class': 'mb-0'}))
    username = forms.CharField(max_length=150, label='Логин', required=False, widget=forms.TextInput(attrs={'placeholder': 'Юзернейм', 'class': 'mb-0'}))
    password = forms.CharField(max_length=150, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'mb-0'}))
    ref_code = forms.CharField(max_length=150, required=False, widget=forms.TextInput(attrs={'placeholder': 'Реф. код', 'class': 'mb-0'}))
    agreed = forms.CharField(required=False, widget=forms.CheckboxInput(attrs={'class': 'mr-1'}))
    captcha = CaptchaField(required=False, widget=CustomCaptchaTextInput(attrs={'placeholder': 'Код с картинки', 'class': 'mt-3'}), error_messages={'invalid': 'Вы не прошли капчу'})
    secure_code = forms.CharField(max_length=150, required=False, widget=forms.TextInput())

    class Meta:
        model = UserProfile
        fields = ['login', 'username', 'password', 'ref_code', 'agreed', 'secure_code']

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if not login:
            raise ValidationError('Вы должны заполнить поля!')
        return login

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise ValidationError('Вы должны заполнить поля!')
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('Вы должны заполнить поля!')
        return password

    # def clean_ref_code(self):
    #     ref_code = self.cleaned_data.get('ref_code')
    #     if not ref_code:
    #         raise ValidationError('Вы должны заполнить поля!')
    #     return ref_code

    def clean_agreed(self):
        agreed = self.cleaned_data.get('agreed')
        if not agreed:
            raise ValidationError('Вы должны согласиться с правилами!')
        return agreed

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        if not captcha:
            raise ValidationError('Вы не прошли капчу')
        return captcha


class LoginForm(forms.Form):
    login = forms.CharField(max_length=150, required=False, label='Логин', widget=forms.TextInput(attrs={'placeholder': 'Логин', 'class': 'mb-0'}))
    password = forms.CharField(max_length=150, required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'mb-0'}))
    captcha = CaptchaField(required=False, widget=CustomCaptchaTextInput(attrs={'placeholder': 'Код с картинки', 'class': 'mt-3'}), error_messages={'invalid': 'Вы не прошли капчу'})

    def clean_login(self):
        login = self.cleaned_data.get('login')
        if not login:
            raise ValidationError('Вы должны заполнить поля!')
        return login

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError('Вы должны заполнить поля!')
        return password

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        if not captcha:
            raise ValidationError('Вы не прошли капчу')
        return captcha




    # def clean_captcha(self):
    #     captcha = self.cleaned_data.get('captcha')
    #     if not captcha:
    #         raise ValidationError('заполни')
    #     return captcha
# class UserForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['login', 'username', 'password', 'ref_code', 'agreed']
#         widgets = {
#             'login': forms.TextInput(attrs={'placeholder': 'Логин'}),
#             'username': forms.TextInput(attrs={'placeholder': 'Юзернейм'}),
#             'password': forms.PasswordInput(attrs={'placeholder': 'Пароль'}),
#             'ref_code': forms.TextInput(attrs={'placeholder': 'Реф. код'}),
#             'agreed': forms.CheckboxInput(attrs={'class': 'mr-1'})
#         }
#
#     def clean_title(self):
#         login = self.cleaned_data['login']
#         if login is None:
#             raise ValidationError('заполни')
#         return login
        # error_messages = {
        #     'login': {
        #         'required': "Вы должны заполнить поля!",
        #     },
        #     'username': {
        #         'required': "Вы должны заполнить поля!",
        #     },
        #     'password': {
        #         'required': "Вы должны заполнить поля!",
        #     },
        #     'ref_code': {
        #         'required': "Вы должны заполнить поля!",
        #     },
        #     'agreed': {
        #         'required': "Вы должны согласиться с правилами!",
        #     }
        #
        #
        # }





