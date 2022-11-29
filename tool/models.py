from turtle import back
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100,verbose_name="Company Name",blank=True,null=True)
    code = models.CharField(max_length=10,verbose_name="Company Code",blank=True,null=True,unique=True)
    timestamp = models.DateTimeField(verbose_name="Created Date and Time",auto_now_add=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering =["-timestamp"]
    
class Product(models.Model):
    name = models.CharField(max_length=500,verbose_name="Name of Product",blank=True,null=True)
    serial_no = models.PositiveIntegerField(blank=True,null=True,verbose_name="Product Code")
    quantity = models.PositiveIntegerField(verbose_name="Quantitty",blank=True,null=True,default=0)
    price = models.PositiveIntegerField(verbose_name="Price",blank=True,null=True)
    disc = models.TextField(verbose_name="Description",blank=True,null=True)
    company = models.ForeignKey(Company,verbose_name="Company Name",on_delete=models.CASCADE)
    timestamp = models.DateTimeField(verbose_name="Product Added On",auto_now_add=True,blank=True,null=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering =["-timestamp"]

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    img = models.ImageField(verbose_name="image")
    timestamp = models.DateTimeField(verbose_name="Image Added On",auto_now_add=True,blank=True,null=True)
    def __str__(self) -> str:
        return self.product.name
    class Meta:
        ordering =["-timestamp"]

