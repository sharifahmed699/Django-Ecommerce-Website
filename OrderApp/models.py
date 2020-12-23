from django.db import models
from Product.models import Product
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.safestring import mark_safe

# Create your models here.

class ShopCart(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity=models.IntegerField()

    def price(self):
        return self.product.new_price
    
    @property
    def amount(self):
        return self.quantity*self.product.new_price


    def __str__(self):
        return self.product.title

class ShopingCartForm(ModelForm):
    class Meta:
        model=ShopCart
        fields=['quantity']


class Order(models.Model):
    status=(
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Onshiping', 'Onshiping'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),

    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    code=models.CharField(max_length=200,editable=False)
    phone=models.CharField(max_length=200,blank=True)
    address=models.CharField(max_length=200,blank=True)
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200,blank=True)
    total=models.FloatField()
    status=models.CharField(max_length=20, choices=status,default='New')
    ip=models.CharField(max_length=200,blank=True)
    transaction_id=models.CharField(max_length=200,blank=True)
    transaction_image=models.ImageField(upload_to='transaction_image/',blank=True)
    adminnote=models.CharField(max_length=200, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','phone','address','city','country','transaction_id','transaction_image']

class OrderProduct(models.Model):
    status=(
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Cancelled', 'Cancelled'),
    )
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.FloatField()
    amount=models.FloatField()
    status=models.CharField(max_length=20, choices=status,default='New')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title
    
    def amountnow(self):
        return self.price*self.quantity
