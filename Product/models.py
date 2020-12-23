from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.db.models import Sum,Avg,Count

# Create your models here.
class Category(MPTTModel):
    status=(
        ('True', 'True'),
        ('False', 'false'),
    )
    parent=TreeForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    title=models.CharField(max_length=200)
    keyword=models.CharField(max_length=100)
    image=models.ImageField(blank=True, upload_to='category/')
    status=models.CharField(max_length=20, choices=status)
    slug=models.SlugField(null=True,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        return self.title

class Product(models.Model):
    status=(
        ('True', 'True'),
        ('False', 'false'),
    )
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    keyword=models.CharField(max_length=100)
    image=models.ImageField(blank=True, upload_to='product/')
    new_price=models.DecimalField(decimal_places=2,max_digits=15, default=0)
    old_price=models.DecimalField(decimal_places=2,max_digits=15)
    amount=models.IntegerField(default=0)
    min_amount=models.IntegerField(default=3)
    detail=models.TextField()
    status=models.CharField(max_length=20, choices=status)
    slug=models.SlugField(null=True,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def ImageUrl(self):
        if self.image:
            return self.image.url
        else:
            return ""

    def get_absolute_url(self):
        return reverse('product_element',kwagrs={'slug':self.slug})
    def image_tag(self):
        return mark_safe('<img src="{}" heights="70" width="60" />'.format(self.image.url))
    image_tag.short_description = 'Image'


    def avg_review(self):
        reviews=Comment.objects.filter(product=self, status=True).aggregate(average=Avg('rate'))
        avg=0
        if reviews['average'] is not None:
            avg=float(reviews['average'])
            return avg
        else:
            return avg

    
    def total_review(self):
        reviews=Comment.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        cunt=0
        if reviews['count'] is not None:
            cunt=(reviews['count'])
            return cunt

  


class Images(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    title=models.TextField(max_length=200, blank=True)
    image=models.ImageField(blank=True,upload_to='product/')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    status=(
        ('New','New'),
        ('True', 'True'),
        ('False', 'false'),
    )
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    subject=models.CharField(max_length=200,blank=True)
    comment=models.CharField(max_length=500,blank=True)
    rate=models.IntegerField()
    status=models.CharField(max_length=20, choices=status,default='New')
    ip=models.CharField(max_length=200,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject


class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['subject','comment','rate']