import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app1 import models
from app1.utils.pagination import Pagination
from app1.utils.form import UserModelForm, NumberEditModelForm, NumberModelForm


# Create your views here.
def depart_list(request):

    queryset = models.Department.objects.all()

    page_obj = Pagination(request, queryset, page_size=10)
    context = {
        "depart_list": page_obj.page_queryset,
        'page_string': page_obj.html(),
    }

    return render(request, 'depart_list.html', context)
def depart_add(request):

    if request.method == 'GET':
        return render(request, 'depart_add.html')
    else:
        title = request.POST.get('title')
        models.Department.objects.create(title=title)
        return redirect('/depart/list')
def depart_del(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()

    return redirect('/depart/list')
def depart_edit(request, nid):
    if request.method == 'GET':
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_edit.html', {'row_object': row_object})
    else:
        models.Department.objects.filter(id=nid).update(title=request.POST.get('title'))
        return redirect('/depart/list')

def depart_multi(request):

    file_obj = request.FILES.get("exc")

    # wb = load_workbook(file_obj)
    # sheet = wb.sheet[0]
    #
    # for row in sheet.iter_rows(min_row=2):
    #     text = row[0].value
    #
    #     models.Department.objects.create(title=text)
    df = pd.read_excel(file_obj)

    for index, row in df.iterrows():
        text = row[0]
        if not models.Department.objects.filter(title=text).exists():
            models.Department.objects.create(title=text)

    return redirect('/depart/list')