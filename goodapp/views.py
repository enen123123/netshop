from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views import View

from goodapp.models import Category,Goods

class Indexview(View):
    def get(self,request,cid=1,num=1):
        cid=int(cid)
        num=int(num)
        # 查询所有类别信息
        categorylist=Category.objects.all()
        # 查询当前分类下的商品信息
        # 商品数量太少，无法体现部分功能，但是已经设置
        goodslist=Goods.objects.filter(category_id=cid).order_by('id')
        # 创建分页对象,数量
        paginator_obj=Paginator(goodslist,8)
        # 创建某一页的数据对象
        page_obj=paginator_obj.page(num)
        # 页数设置
        begin=num-int(3)
        if begin<1:
            begin=1
        end=begin+5
        if end>paginator_obj.num_pages:
            end=paginator_obj.num_pages
        if end<6:
            begin=1
        else:
            begin=end-5
        pagelist=range(begin,end+1)

        return render(request,'index.html',{'categorylist':categorylist,'cid':cid,'goodslist':page_obj,'pagelist':pagelist})

def randomgoodsview(func):
    def _wrapper(detailview,request,goodsid,*args,**kwargs):
        # 从cookie获取用户访问信息
        cgoodsid=request.COOKIES.get('rem','')
        # 记录用户访问过的商品id
        # ['1','2','3']='1 2 3'
        # gid.strip() 去除空格等信息
        goodsidlist=[gid for gid in cgoodsid.split() if gid.strip()]
        # 最终产品列表
        # 这里我无法做到将数据列表做到完美切分并一次传递，只得将其分开提取并组合
        # 判断一下历史记录是否为空，
        if len(goodsidlist)<2:
            # 当显示默认的历史记录时为默认值，证明没有历史记录
            goodsidlist=['1', '2']
        goodsobjlist = [Goods.objects.get(id=goodsidlist[0]), Goods.objects.get(id=goodsidlist[1])]
        # print(goodsidlist)
        # 调用相应修饰函的数
        response=func(detailview,request,goodsid,goodsobjlist,*args,**kwargs)
        # 判断用户访问商品,将新加入的作为顺序第一个，重复移除
        if goodsid in goodsidlist:
            goodsidlist.remove(goodsid)
            goodsidlist.insert(0,goodsid)
        else:
            goodsidlist.insert(0,goodsid)
        # ''.join将列表转换为一个字符串
        # 将用户访问的商品id存放在cookie缓存
        response.set_cookie('rem',' '.join(goodsidlist),max_age=3600*24)
        return response
    return _wrapper

class Detailview(View):
    # 设置一个随机推荐的装饰器
    @randomgoodsview
    def get(self,request,goodsid,recommendlist=[]):
        goodsid=int(goodsid)
        # 根据商品id查询
        goods=Goods.objects.get(id=goodsid)

        return render(request,'detail.html',{'goods':goods,'recommendlist':recommendlist})


def aboutview(request):
    # 关于声明
    return render(request,'about.html')