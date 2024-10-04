from absl.flags import ValidationError
from django.core.validators import RegexValidator
from django import forms
from app1 import models
from app1.utils.bootstrap import BootstrapModelForm

class UserModelForm(BootstrapModelForm):
    name = forms.CharField(
        min_length=3,
        label='用户名',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = models.UserInfo
        fields = ['name', 'password', 'age', 'account', 'create_time', 'gender', 'depart']
        widgets = {
            "password": forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class NumberModelForm(BootstrapModelForm):
    mobile = forms.CharField(label='手机号', required=True,
                             validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ])
    price = forms.IntegerField(label='价格', required=True, min_value=0)

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']


    def clean_mobile(self):
        text = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.filter(mobile=text).exists()
        if exists:
            raise ValidationError('手机号已存在')
        return text

class NumberEditModelForm(BootstrapModelForm):
    mobile = forms.CharField(label='手机号', required=True,
                             validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ])
    price = forms.IntegerField(label='价格', required=True, min_value=0)

    class Meta:
        model = models.PrettyNum
        fields = ['mobile', 'price', 'level', 'status']

    def clean_mobile(self):

        text = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=text).exists()
        if exists:
            raise ValidationError('手机号已存在')
        return text