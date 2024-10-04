from django.shortcuts import render, redirect
from app1 import models
from app1.utils.pagination import Pagination
from app1.utils.encrypt import md5



def admin_list(request):
    # for i in range(10):
    #     models.Admin.objects.create(username='123', password='123456')
    info = request.session.get('info')
    if not info:
        return redirect('login')

    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['username__contains'] = search_data

    queryset = models.Admin.objects.all().filter(**data_dict)

    page_object = Pagination(request, queryset)
    context = {
        'admin_list': page_object.page_queryset,  # 分完页的数据
        'page_string': page_object.html(),  # 生成页码
    }

    return render(request, 'admin_list.html', context)


from django import forms
from app1.utils.bootstrap import BootstrapModelForm
class AdminModelForm(BootstrapModelForm):

    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput)
    class Meta:
        model = models.Admin
        fields = ['username', 'password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        return md5(password)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        if password != confirm_password:
            raise forms.ValidationError('密码不一致')
        else:
            return confirm_password

class AdminEditModelForm(BootstrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']

class AdminResetModelForm(BootstrapModelForm):
    confirm_password = forms.CharField(label='确认密码', widget=forms.PasswordInput)
    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            'password': forms.PasswordInput
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        md5_password = md5(password)

        if models.Admin.objects.filter(id=self.instance.pk, password=md5_password).exists():
            raise forms.ValidationError('密码与之前的相同')

        return md5_password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = md5(self.cleaned_data.get('confirm_password'))
        if password != confirm_password:
            raise forms.ValidationError('密码不一致')
        else:
            return confirm_password
def admin_add(request):

    title = '新建管理员'

    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'change.html', {'form': form, "title": title})
    else:
        form = AdminModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/admin/list')
        else:
            print(form.errors)
            return render(request, 'change.html', {'form': form, "title": title})


def admin_edit(request, nid):

    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'admin_list.html')

    title = '编辑管理员'
    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'change.html', {'form': form, "title": title})
    else:
        form = AdminEditModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect('/admin/list')
        else:
            print(form.errors)
            return render(request, 'change.html', {'form': form, "title": title})

def admin_del(request, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list')

def admin_reset(request, nid):

    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return render(request, 'admin_list.html')

    title = '重置密码 - {}'.format(row_object.username)

    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'change.html', {"form": form, "title": title})
    else:
        form = AdminResetModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect('/admin/list')
        else:
            print(form.errors)
            return render(request, 'change.html', {"form": form, "title": title})
