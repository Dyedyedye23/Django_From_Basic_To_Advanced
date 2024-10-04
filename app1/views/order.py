import random

from django.shortcuts import render
from app1 import models
from app1.utils.bootstrap import BootstrapModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from app1.utils.pagination import Pagination


class OrderModelForm(BootstrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ['oid', 'admin']

def order_list(request):
    form = OrderModelForm()
    queryset = models.Order.objects.all().order_by('-id')
    page_obj = Pagination(request, queryset, page_size=10)
    context = {
        'form': form,
        "order_list": page_obj.page_queryset,
        'page_string': page_obj.html(),
    }

    return render(request, 'order_list.html', context)

@csrf_exempt
def order_add(request):
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        form.instance.oid = datetime.now().strftime('%Y%m%d%H%M%S') + str(random.randint(1000, 9999))
        form.instance.admin_id = request.session['info']['id']
        form.save()
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors})

def order_del(request):
    nid = request.GET.get('nid')
    print(nid)
    if not models.Order.objects.filter(id=nid).exists():
        return JsonResponse({'status': False, 'error': '删除失败，数据不存在'})

    models.Order.objects.filter(id=nid).delete()
    return JsonResponse({'status': True})

def order_detail(request):
    nid = request.GET.get('nid')
    print(nid)
    order_dict = models.Order.objects.filter(id=nid).values('title', 'price', 'status').first()
    if not order_dict:
        return JsonResponse({'status': False, 'error': '数据不存在'})

    result = {
        'status': True,
        'data': order_dict
    }

    return JsonResponse(result)

@csrf_exempt
def order_edit(request):

    nid = request.GET.get('nid')
    print(nid)
    row_obj = models.Order.objects.filter(id=nid).first()
    if not row_obj:
        return JsonResponse({'status': False, 'tips': '数据不存在'})

    form = OrderModelForm(data=request.POST, instance=row_obj)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': True})

    return JsonResponse({'status': False, 'error': form.errors})
