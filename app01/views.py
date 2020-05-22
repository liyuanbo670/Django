from django.shortcuts import render,HttpResponse,redirect
from app01.models import Book
from django.urls import reverse

# Create your views here.

def addbook(request):
    # book = Book(nid=1,price=234,title='python',publish="电子工业出版社",pub_date="2012-12-12")
    # book.save()
    # book = Book.objects.create(title='C++',price=222,pub_date='2020-10-10',publish='中国人民出版社')
    # print(book.nid,book.title)
    if request.method=="POST":
        # title = request.POST.get("title")
        # price = request.POST.get("price")
        # publish = request.POST.get("publish")
        # pub_date = request.POST.get("pub_date")
        # book = Book.objects.create(title=title,price=price,publish=publish,pub_date=pub_date)
        # del request.POST["csrfmiddlewaretoken"]
        data = request.POST.dict() # 将request.POST(queryset类型)转换为字典
        # print(data)
        del data["csrfmiddlewaretoken"] # 将字典中的k='csrfmiddlewaretoken'元素删掉
        book = Book.objects.create(**data)
        return redirect(reverse("books"))
    else:
        return render(request,'addbook.html')


def books(request):
    book_list=Book.objects.all()
    return render(request,"books.html",{"book_list":book_list})

def delbook(request,delete_book_id):
    Book.objects.filter(nid=delete_book_id).delete()
    return redirect(reverse("books"))

def editbook(request,edit_book_id):
    """
    编辑功能
    :param request:
    :param edit_book_id:
    :return:
    """
    edit_book = Book.objects.filter(nid=edit_book_id)[0]
    if request.method=='POST':
        title=request.POST.get("title")
        price=request.POST.get("price")
        publish=request.POST.get("publish")
        pub_date=request.POST.get("pub_date")
        Book.objects.filter(nid=edit_book_id).update(title=title,price=price,publish=publish,pub_date=pub_date)
        return redirect(reverse("books"))
    else:
        return render(request,"editbook.html",{"edit_book":edit_book})

# ******************************************************************************************************
def  query(request):
    # ret = Book.objects.filter(title="go",price=3)
    # ret = Book.objects.all()
    # ret = Book.objects.get(price=123)
    # ret = Book.objects.all()[1]
    # ret = Book.objects.exclude(price=123)
    # ret = Book.objects.all().order_by("-price")
    # ret = Book.objects.all().exists()
    # if ret:
    #     print("ok")
    # ret = Book.objects.all().filter(price__gt=200)
    # ret = Book.objects.filter(price__lt=200)
    # ret = Book.objects.filter(title__contains="n").values("title")
    ret = Book.objects.filter(pub_date__year=2012,pub_date__month=12).values("title")
    print(ret)
    return HttpResponse("查询成功")
