from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

# from cartapp.cartmanager import getcartmanger
from cartapp.models import Cartitem


class Cartview(View):
    def post(self,request):

        # 获取全局上下文中的账号
        user = request.session.get('user')
        # 获取当前用户操作数据类型
        colorid = request.POST.get('colorid','')
        goodsid = request.POST.get('goodsid','')
        sizeid = request.POST.get('sizeid','')
        count = request.POST.get('count','')
        flag = request.POST.get('flag','')

        # print(colorid,goodsid,sizeid,count,flag)


#         判断用户当前操作类型
        if flag == 'add':
            Cartitem.objects.create(goodsid=goodsid,colorid=colorid,sizeid=sizeid,count=count,user=user)
            # 获取对象
            # cartmanger=getcartmanger(request)
            # 加入购物车
            # cartmanger.add(**request.POST.dict())
        # return HttpResponse('加入购物车成功')
        return HttpResponseRedirect('/cart/queryall/')


def queryall(request):
    # 获取全局上下文中的账号
    user = request.session.get('user')
    # 获取对应用户下的购物表内容
    cartitemlist=Cartitem.objects.filter(user_id=user.id).all()
    return render(request,'manager.html',{'cartitemlist':cartitemlist})


def deletequery(request,cartitemid):
    # 获取全局上下文中的账号
    user = request.session.get('user')
    # 删除指定的项，然后展示
    Cartitem.objects.filter(user_id=user.id,id=cartitemid).delete()
    cartitemlist=Cartitem.objects.filter(user_id=user.id).all()
    return render(request, 'manager.html', {'cartitemlist': cartitemlist})


