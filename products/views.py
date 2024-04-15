from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def Productdetails(request):
    obj = Product.objects.all()
    return render(request,"pview.html",{"data":obj})
def Productedit(request):
    userid = request.GET.get('uid')
    obb = Product.objects.filter(id=userid)
    return render(request,"productview.html",{"prod":obb})
def Productupdate(request):
    if request.method=='POST':
        nm = request.POST.get('name')
        idno = request.POST.get('uid')
        desc = request.POST.get('desc')
        price = request.POST.get('ps')
        Product.objects.filter(id=idno).update(name=nm,description=desc,price=price)
        return redirect("/fileApi/ProductDetails")
    return render(request,"productview.html")
def delete(request):
    userid = request.GET.get('uid')
    obb = Product.objects.filter(id=userid)
    obb.delete()
    return redirect("/products/ProductDetails")

