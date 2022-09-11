# sessionquanjvhuancun

def getsessioninfo(request):
    return {'user':request.session.get('user','')}


