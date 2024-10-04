from django.http import JsonResponse
from django.shortcuts import render


def chart_list(request):
    return render(request, 'chart_list.html')


def chart_bar(request):
    legend = ['手机', '电脑']
    series_list = [
        {
            'name': '手机',
            'type': 'bar',
            'data': [5, 20, 36, 10, 10, 20]
        },
        {
            'name': '电脑',
            'type': 'bar',
            'data': [15, 10, 16, 20, 30, 40]
        }
    ]
    x_axis = ['1月', '2月', '3月', '4月', '5月', '6月']

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis,
        }
    }

    return JsonResponse(result)


def chart_pie(request):
    db_data_list = [
        {"name": "直接访问", "value": 335},
        {"name": "邮件营销", "value": 310},
        {"name": "联盟广告", "value": 234},
        {"name": "视频广告", "value": 135},
        {"name": "搜索引擎", "value": 1548}
    ]

    result = {
        "status": True,
        "data": db_data_list,
    }

    return JsonResponse(result)


def chart_line(request):
    legend = ['邮件营销', '联盟广告', '视频广告',]
    series_list = [
        {
            'name': '邮件营销',
            'type': 'line',
            'stack': 'Total',
            'data': [120, 132, 101, 134, 90, 230, 210]
        },
        {
            'name': '联盟广告',
            'type': 'line',
            'stack': 'Total',
            'data': [220, 182, 191, 234, 290, 330, 310]
        },
        {
            'name': '视频广告',
            'type': 'line',
            'stack': 'Total',
            'data': [230, 382, 291, 334, 390, 330, 320]
        }
    ]
    x_axis = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

    result = {
        "status": True,
        "data": {
            "legend": legend,
            "series_list": series_list,
            "x_axis": x_axis,
        }
    }

    return JsonResponse(result)
