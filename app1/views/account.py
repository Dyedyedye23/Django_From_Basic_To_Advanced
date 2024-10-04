from django.shortcuts import render, redirect

from django import forms

from app1 import models
from app1.utils.bootstrap import BootstrapForm
from app1.utils.encrypt import md5


class LoginForm(BootstrapForm):
    username = forms.CharField(label='用户名', max_length=32, widget=forms.TextInput)
    password = forms.CharField(label='密码', max_length=32, widget=forms.PasswordInput)

    def clean_password(self):
        pwd = self.cleaned_data.get('password')
        return md5(pwd)
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(data=request.POST)
        if form.is_valid():
            admin_obj = models.Admin.objects.filter(**form.cleaned_data).first()
            if not admin_obj:
                form.add_error('password', '用户名或密码错误')
                return render(request, 'login.html', {'form': form})
            request.session['info'] = {'id': admin_obj.id, 'name': admin_obj.username}
            return redirect('/admin/list')


        print(form.errors)
        return render(request, 'login.html', {'form': form})

def logout(request):
    request.session.clear()
    return redirect('/login')
