from .models import Application, User, Category
from django import forms
from django.core.validators import RegexValidator, EmailValidator


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput,
                               validators=[RegexValidator(r'[a-zA-Z\-]', 'В логине доступны только латинские символы')],
                               required=True)

    full_name = forms.CharField(label='ФИО', widget=forms.TextInput,
                                validators=[RegexValidator(r'[а-яА-ЯёЁ\-\s]',
                                                           'В ФИО доступна только кириллица, пробелы и дефис')],
                                required=True)

    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput, required=True)
    email = forms.EmailField(label='Email', widget=forms.EmailInput, required=True,
                             validators=[EmailValidator('Email не верен')])
    checkbox = forms.CharField(label='Согласие на обработку персональных данных', widget=forms.CheckboxInput,
                               required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'full_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']

    def clean_checkbox(self):
        cd = self.cleaned_data
        print(cd['checkbox'])
        if cd['checkbox'] == False:
            raise forms.ValidationError('Подтвердите обработку персональных данных')
        return cd['checkbox']


class ApplicationCreateForm(forms.ModelForm):
    title = forms.CharField(label='Название', widget=forms.TextInput)
    desc = forms.CharField(label='Описание', widget=forms.TextInput)

    class Meta:
        model = Application
        fields = ('title', 'desc', 'img')


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
