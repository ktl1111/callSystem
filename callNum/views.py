from django.contrib import messages
from django.shortcuts import render
from .models import Number, OnspotNum
from django.contrib.auth.decorators import login_required
# Create your views here.


def all_nums(request):
    num_list = Number.objects.all().order_by("-stamp")[:1]
    num_list = reversed(num_list)

    onspotNum_list = OnspotNum.objects.all().order_by("-onspot_stamp")[:1]
    onspotNum_list = reversed(onspotNum_list)

    return render(request, 'call.html', {
        'num_list': num_list,
        'onspotNum_list': onspotNum_list,
    })


def index(request):
    return render(request, 'index.html', {})


@login_required
def portal(request):
    num_list = Number.objects.all()
    if request.POST.get('number'):
        try:
            print('IN!')
            num = Number()
            num.num = request.POST.get('number')
            num.save()
            print("input1")
            messages.info(request, '線上叫號成功')
            return render(request, 'portal.html', {
                "num": num,
                "num_list": num_list,
            })
        except:
            return render(request, 'portal.html')
            print('error online')
    else:
        return render(request, 'portal_onspot.html', {
            "num_list": num_list,
        })

@login_required
def portal_onspot(request):
    onspotNum_list = OnspotNum.objects.all()
    if request.POST.get('onspot_number'):
        try:
            onspotNum = OnspotNum()
            onspotNum.onspot_num = request.POST.get('onspot_number')
            onspotNum.save()
            return render(request, 'portal_onspot.html', {
                "onspotNum": onspotNum,
                "onspotNum_list": onspotNum_list,
            })
        except:
            return render(request, 'portal.html')
            print('error online')
    else:
        return render(request, 'portal.html', {
            "onspotNum_list": onspotNum_list,
        })

# def portal_list_num(request):
#     num_list = Number.objects.all().order_by("-stamp")
#     num_list = reversed(num_list)
#
#     onspotNum_list = OnspotNum.objects.all().order_by("-stamp")
#     onspotNum_list = reversed(onspotNum_list)
#
#     return render(request, 'portal.html', {
#         'num_list': num_list,
#         'onspotNum_list': onspotNum_list,
#     })
