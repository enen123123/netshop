import json

from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render


def orderview(request):
    # 传递购物车页面提交的信息
    cartitems=request.GET.get('cartitems','')
    # print (cartitems)
    user = request.session.get('user', '')
    # 将获得的信息反序列化,字符串转化成列表
    cartitemslist=json.loads(cartitems)
    # print(cartitems)
    # print(cartitemslist)
    # print(type(cartitems))
    # print(type(cartitemslist))
    # user.cartitem_set.get(**ci) 根据获取的用户、参数，获取购物车表中的列表
    cartitemsobjlist=[ user.cartitem_set.get(**ci) for ci in cartitemslist if ci]
    # 只有子表才有"子表名小写_set"的写法,得到的是一个QuerySet集合
    # 获取用户默认收件地址
    addr=user.address_set.get(isdefault=True)

    # 支付总金额
    totalprice=0
    for cio in cartitemsobjlist:
        totalprice=totalprice+cio.gettotalprice()

    # return render(request,'order.html')
    return render(request,'order.html',{'cartitemslist':cartitemsobjlist,'addr':addr,'totalprice':totalprice})

