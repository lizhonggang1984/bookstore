from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.template import loader, RequestContext
from booktest.models import BookInfo,HeroInfo,AreaInfo
from datetime import date
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def login(request):
    if request.session.get('islogin',False) == True:
        return HttpResponseRedirect('/index')
    else:
        if 'username' in request.COOKIES:
            username=request.COOKIES['username']
        else:
            username=''
        return render(request,'booktest/login.html',{'username':username})

@csrf_exempt
def login_check(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

    else:
        username = request.GET.get('username')
        password = request.GET.get('password')
        remember = request.GET.get('remember')

    if username== 'python' and password == 'chuanzhi':
        response = HttpResponseRedirect('/index')
        if (remember=='on'):
            response.set_cookie('username',username,max_age=7*24*60*60)

        request.session['islogin'] = True
        request.session.set_expiry(0)
        return response
    else:
        return HttpResponseRedirect('/login')


def index2(request):
    # setup template
    template = loader.get_template('booktest/index2.html')
    # context_dict to pass
    context_dict = RequestContext(request,{}).flatten()
    # render context
    res_html = template.render(context_dict)

    return HttpResponse(res_html)

def index3(request):
    # setup template
    template = loader.get_template('booktest/index3.html')
    # context_dict to pass
    mydict = {'title':'dictTitle','content':'dictContent','id':'dictID'}
    mylist= [1,2,3]
    book= BookInfo.objects.get(id=1)
    books = BookInfo.objects.all()
    context_dict = RequestContext(request,{'mydict':mydict,'mylist':mylist,'book':book,'books':books}).flatten()
    # render context
    res_html = template.render(context_dict)

    return HttpResponse(res_html)


def index(request):
    # num = "a" + 1
    return render(request,'booktest/index.html')

def books(request):
    books = BookInfo.objects.all()
    return render(request,'booktest/books.html',{'books':books})

def create(request):
    book = BookInfo()
    book.btitle = 'liuxinghudiejian'
    book.bpub_date = date(1990,1,1)
    book.bcomment = 15
    book.bread = 10
    book.save()
    return HttpResponseRedirect('/index')

def delete(request,bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    return HttpResponseRedirect('/index')

def areas(request):
    area = AreaInfo.objects.get(atitle='xijiang')
    parent = area.aParent
    children = area.areainfo_set.all()
    # templates
    return render(request, 'booktest/areas.html', {'area':area,'parent':parent, 'children':children})

def showArg(request,param):
    return HttpResponse(param)

def ajax_test(request):
    return render(request,'booktest/test_ajax.html')

def ajax_handle(request):
    return JsonResponse({'res':1})

@csrf_exempt
def login_ajax(request):
    return render(request,'booktest/login_ajax.html')

@csrf_exempt
def login_ajax_check(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    else:
        username = request.GET.get('username')
        password = request.GET.get('password')

    if username== 'python' and password == 'chuanzhi':
        return JsonResponse({'res': 1})
    else:
        return JsonResponse({'res': 0})

def set_cookie(request):
    response = HttpResponse('set up cookie')
    response.set_cookie('num',1,max_age=60*5)
    return response

def get_cookie(request):
    num = request.COOKIES['num']
    return HttpResponse(num)

# def set_session(request):
#     request.session['username'] = 'python'
#     request.session['age'] = 18
#
#     request.session.set_expiry(0) # expire for shutting down explorer
#
#     return HttpResponse('set up session')
# def get_session(request):
#     username = request.session.get('username',"username not setup")
#     age = request.session.get('age',"age not setup")
#     return HttpResponse(username + " : " + str(age))

def child(request):
    return render(request, 'booktest/child.html')


