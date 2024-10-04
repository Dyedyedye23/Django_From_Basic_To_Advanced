from django.shortcuts import render, redirect
from app1 import models
from app1.utils.pagination import Pagination
from app1.utils.form import UserModelForm, NumberEditModelForm, NumberModelForm


# Create your views here.
def user_list(request):

    queryset = models.UserInfo.objects.all()

    page_obj = Pagination(request, queryset, page_size=10)
    context = {
        "user_list": page_obj.page_queryset,
        'page_string': page_obj.html(),
    }

    return render(request, 'user_list.html', context)
def user_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_add.html', {'form': form})
    else:
        form = UserModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/user/list')
        else:
            print(form.errors)
            return render(request, 'user_add.html', {'form': form})
def user_edit(request, nid):
    row_object = models.UserInfo.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})
    else:
        form = UserModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect('/user/list')
        else:
            print(form.errors)
            return render(request, 'user_edit.html', {'form': form})
def user_del(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')
