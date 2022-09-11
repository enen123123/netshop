#coding=utf-8
from goodapp.models import*
from django.db.transaction import atomic   #事物
@atomic
def test_model( ):
    # 没有该数据库文件，需要自己配置到mysql
    # 其本质就是将抓取的文件放入mysql
    with open('utils/jiukuaijiu.json') as fr:
        import json
        datas = json.loads(fr.read())
        for data in datas:
            cate = Category.objects.create(cname=data["category"])
            _goods = data['goods']
            for goods in _goods :
                good=Goods.objects.create(gname=goods['goodsname'],gdesc=goods['goods_dessc'],
                                          price=goods['goods_price'],oldprice=goods['goods_oldprice'],
                                          category=cate)
                sizes=[]
                for _size in goods['size']:
                    if Size.objects.filter(sname=_size[0].count()==1):
                        size=Size.objects.get(sname=_size[0])
                    else:
                        size=Size.objects.create(sname=_size[0])
                    sizes.append(size)

                colors=[]
                for _color in goods['colors']:
                    color = Color.objects.create(colorname=_color[0], colorurl=_color[1])
                    colors.append(color)

                for _spec in goods['specs']:
                    goodsdetails = Gooddeatilname.objects.create(gdname=_spec[0])
                    for img in _spec[1]:
                        Gooddeatil.objects.create(goods=good, goodsdname=goodsdetails, gdurl=img)
                for c in colors:
                    for s in sizes:
                        Inventory.objects.create(count=100, goods=good, color=c, size=s)


def deleteall():
    Category.objects.filter().delete()
    Color.objects.fi1ter().delete()
    Size.objects.filter().delete()




