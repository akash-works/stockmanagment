from itertools import product
from wsgiref import validate
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages


def home(request):
    context = {
        "products":Product.objects.all()
    }

    return render(request,"home.html",context)

def add_company(request):
    if request.method=="POST":
        name = request.POST["name"]
        code = request.POST["code"]
        obj = Company.objects.create(name=name,code=code)
        if obj:
            messages.success(request,"Successfully Added")
            return redirect("home")
        messages.error(request,"somthing went wrong")
    return redirect("home")



def add_product(request):
    if request.method=="POST":
        name = request.POST["name"]
        s_no = request.POST["serial_no"]
        quantity = request.POST["quantity"]
        price = request.POST["price"]
        code = request.POST["comapny_code"]
        img = request.FILES.get("image")
        desc = request.POST["description"]
        company = Company.objects.get(code=code)
        obj = Product.objects.create(name=name,serial_no=s_no,quantity=quantity,price=price,company=company,disc=desc)
        if obj:
            obj_imge = ProductImage.objects.create(product=obj,img=img)
            if obj_imge: 
                messages.success(request,"Successfully Added")
                return redirect("home")
        messages.error(request,"somthing went wrong")
    return redirect("home")


def product_detail(request,pk):
    product = ProductImage.objects.get(product__id=pk)
    data = {"product_obj":product}
    return render(request,"product_detail.html",data)

def product_delete(request,pk):
    product = ProductImage.objects.get(product__id=pk)
    product.product.delete()
    product.delete()
    return redirect("home")

def product_update(request, pk,instance,validate_data): 
    product =ProductImage.objects.get(product_id=pk)(instance=product)

    if request.method=="POST":
        instance_name = validate_data.PUT["name".instance.name]
        instance_s_no = validate_data.PUt["serial_no".instance.s_no]
        instance_quantity = validate_data.PUT["quantity".instance.name]
        instance_price = validate_data.PUT["price".instance.name]
        instance_code = validate_data.PUT["comapny_code".instance.name]
        instance_img = validate_data.FILES.get("image".instance.name)
        instance_desc = validate_data.PUT["description".instance.name]
        instance_company = Company.objects.get(code=instance_code)
        obj = Product.objects.create(name=instance_name,serial_no=instance_s_no,quantity=instance_quantity,price=instance_price,company=instance_company,disc=instance_desc)
        instance.save()
        if obj:
            obj_imge = ProductImage.objects.create(product=obj,img=instance_img)
            if obj_imge: 
                messages.success(request,"Successfully Added")
                return redirect("home")
        messages.error(request,"somthing went wrong")
    return render(request,"update_modal.html",product)
   