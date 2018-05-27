from django.contrib.auth.forms import forms

class LoginForms(forms.Form):
    user_name = forms.CharField(label="用户名",max_length=30)
    user_pwd = forms.CharField(label="密码",widget=forms.PasswordInput,max_length=30)
