from django.shortcuts import render, redirect
from app1 import models
from app1.utils.form import UserModelForm, NumberEditModelForm, NumberModelForm

# Create your views here.
def number_list(request):

    # for i in range(300):
    #     models.PrettyNum.objects.create(mobile='14433333333', price=10, level=1, status=1)

    data_dict = {}
    search_data = request.GET.get('q', '')
    if search_data:
        data_dict['mobile__contains'] = search_data

    from app1.utils.pagination import Pagination


    # page = int(request.GET.get('page', 1))
    # start = (page - 1) * 10
    # end = start + 10
    queryset = models.PrettyNum.objects.all().filter(**data_dict).order_by('-level')

    page_obj = Pagination(request, queryset)
    page_queryset = page_obj.page_queryset
    page_string = page_obj.html()

    # total_count = models.PrettyNum.objects.all().filter(**data_dict).count()
    # total_page_count, div = divmod(total_count, 10)
    # if div:
    #     total_page_count += 1
    #
    # plus = 5
    # if total_page_count < 2 * plus + 1:
    #     start_page = 1
    #     end_page = total_page_count + 1
    # else:
    #     if page <= plus:
    #         start_page = 1
    #         end_page = 2 * plus + 1
    #     else:
    #         if page >= total_page_count - plus:
    #             start_page = total_page_count - 2 * plus
    #             end_page = total_page_count + 1
    #         else:
    #             start_page = page - plus
    #             end_page = page + plus + 1
    #
    # page_str_list = []
    #
    # page_str_list.append('<li><a href="?page=1">首页</a></li>')
    #
    # prev = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
    # if page == 1:
    #     prev = '<li class="disabled"><a href="javascript:void(0)">上一页</a></li>'
    # page_str_list.append(prev)
    #
    # for i in range(start_page, end_page):
    #     if i == page:
    #         ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
    #     else:
    #         ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
    #     page_str_list.append(ele)
    #
    # next_page = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    # if page == total_page_count:
    #     next_page = '<li class="disabled"><a href="javascript:void(0)">下一页</a></li>'
    # page_str_list.append(next_page)
    #
    # page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(total_page_count))
    #
    # page_string = mark_safe(''.join(page_str_list))

    context = {
        'number_list': page_queryset,
        'page_string': page_string,
    }

    return render(request, 'number_list.html', context)

def number_add(request):
    if request.method == "GET":
        form = NumberModelForm()
        return render(request, 'number_add.html', {'form': form})
    else:
        form = NumberModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/number/list')
        else:
            print(form.errors)
            return render(request, 'number_add.html', {'form': form})
def number_edit(request, nid):
    row_object = models.PrettyNum.objects.filter(id=nid).first()

    if request.method == 'GET':
        form = NumberEditModelForm(instance=row_object)
        return render(request, 'number_edit.html', {'form': form})
    else:
        form = NumberEditModelForm(data=request.POST, instance=row_object)
        if form.is_valid():
            form.save()
            return redirect('/number/list')
        else:
            print(form.errors)
            return render(request, 'number_edit.html', {'form': form})
def number_del(request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/number/list')