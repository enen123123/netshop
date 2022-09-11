from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from userapp.models import Userinfo, Area


class Registerview(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        # 获取用户名和密码
        acount=request.POST.get('acount','')
        password = request.POST.get('password','')
        #将传递过来的信息存进数据库
        user=Userinfo.objects.create(uname=acount,pwd=password)
        # 判断注册是否成功,成功则返回注册主页面
        if user:
            # 将当前注册用户名保存在session,设置一个全局调用的缓存
            request.session['user']=user
            # HttpResponseRedirect 传递链接     HttpResponse 传递内容
            return HttpResponseRedirect('/user/address/')
            # return HttpResponse('注册成功')
        return HttpResponseRedirect('/user/register/')


class Mainview(View):
    # 用户中心
    def get(self,request):
        return render(request,'main.html')


class Loginview(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        # 获取请求参数
        uname=request.POST.get('acount','')
        pwd=request.POST.get('password','')
        # 查询数据库是否存在用户名
        userlist=Userinfo.objects.filter(uname=uname,pwd=pwd)
        # 判断是否登陆成功
        if userlist:
            request.session['user']=userlist[0]
            # return HttpResponse('登录成功')
            return HttpResponseRedirect('/user/address/')
        return HttpResponseRedirect('/user/login/')

from userapp.models import Address
class Addressview(View):
    def get(self,request):
        # 获取信息
        user = request.session.get('user')
        # 获取创建的所有信息
        addrlist=user.address_set.all()
        # print(addrlist)
        return render(request,'address.html',{'addrlist':addrlist})
    def post(self,request):
        # 获取请求参数
        # print(request.POST)
        # 转化为字典，并移除不必要的信息
        params = request.POST.dict()
        params.pop('csrfmiddlewaretoken')
        # 获取登陆对象和isdefault
        user=request.session.get('user')
        # 传递账户邮箱，以及判断是否为第一个默认账户，和其他信息
        # print(user.id)
        Address.objects.create(userinfo=user,isdefault=(lambda count:True if count == 0 else False)( user.address_set.count()),**params)
        return HttpResponseRedirect('/user/address/')

from django.core.serializers import serialize
from django.http.response import JsonResponse

def loadaddr(request):
    # 获取请求参数
    pid=request.GET.get('pid',-1)
    pid=int(pid)
    # 根据父id查询区划信息
    arealist=Area.objects.filter(parentid=pid)
    # 序列化
    jarealist=serialize('json',arealist)

    return JsonResponse({'jarealist':jarealist})



def deleteaddr(request,addrobjid):

    # 获取信息
    user = request.session.get('user')


    # 删除指定地址
    a=Address.objects.filter(id=addrobjid).delete()
    print(a)
    # 获取创建的所有信息
    addrlist = Address.objects.filter(userinfo_id=user.id).all()
    # print(addrlist)
    return render(request, 'address.html', {'addrlist': addrlist})


