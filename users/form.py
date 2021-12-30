from django import forms

class Login(forms.Form):
    username = forms.CharField(label='User Name', max_length=64, 
    widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput({
        'placeholder': 'Password'
    }))