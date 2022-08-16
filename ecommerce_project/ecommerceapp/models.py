from django.db import models



# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    image = models.ImageField(upload_to='category',blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categoires'

    def get_url(self):
        return  reverse('shop:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='product')
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def get_url(self):
        return reverse('shop:product_detail', args=[self.category.slug,self.slug])

    def __str__(self):
        return  '{}'.format(self.name)