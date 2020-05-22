from django.contrib import admin
from django.urls import path,re_path
from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/add/', views.addbook,name="addbook"),
    path('books/',views.books,name="books"),
    re_path('books/del/(\d+)',views.delbook,name="delbook"),
    re_path('books/edit/(\d+)',views.editbook,name="editbook"),
    path('books/query/',views.query)
]
