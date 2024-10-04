from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from app1 import models
from app1.utils.bootstrap import BootstrapForm, BootstrapModelForm
import os


def upload_list(request):
    if request.method == 'GET':
        return render(request, 'upload_list.html')

    file_obj = request.FILES.get('avatar')

    f = open(file_obj.name, mode='wb')
    for chunk in file_obj.chunks():
        f.write(chunk)
    f.close()

    return HttpResponse('上传成功')

class UploadForm(BootstrapForm):
    bootstrap_exclude_fields = ['img']
    name = forms.CharField(label='姓名')
    age = forms.IntegerField(label='年龄')
    img = forms.FileField(label='头像')

def upload_form(request):

    title = 'Form上传'
    if request.method == 'GET':
        form = UploadForm()
        return render(request, 'upload_form.html', {'form': form, 'title': title})
    form = UploadForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        image_obj = form.cleaned_data.get('img')


        # media_path = os.path.join(settings.MEDIA_ROOT, image_obj.name)
        media_path = os.path.join('media', image_obj.name)
        f = open(media_path, mode='wb')
        for chunk in image_obj.chunks():
            f.write(chunk)
        f.close()

        models.Boss.objects.create(
            name=form.cleaned_data.get('name'),
            age=form.cleaned_data.get('age'),
            img=media_path,
        )

        return HttpResponse('上传成功')
    return render(request, 'upload_form.html', {'form': form, 'title': title})

class UploadModelForm(BootstrapModelForm):
    bootstrap_exclude_fields = ['img']
    class Meta:
        model = models.City
        fields = "__all__"
def upload_model_form(request):
    title = 'ModelForm上传'
    if request.method == 'GET':
        form = UploadModelForm()
        return render(request, 'upload_form.html', {'form': form, 'title': title})

    form = UploadModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        form.save()
        return HttpResponse('上传成功')
    return render(request, 'upload_form.html', {'form': form, 'title': title})