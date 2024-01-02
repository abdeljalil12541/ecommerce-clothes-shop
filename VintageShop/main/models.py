from curses import flash
from random import choices
from turtle import mode
from django.db import models
from django.utils.html import escape, mark_safe
from django.contrib.auth.models import User
from jinja2 import ModuleLoader
from _curses import *
from ngrok import default

# Create your models here.


# Banner 
class Banner(models.Model):
    img      = models.ImageField(max_length=200, upload_to='banner_imgs')
    alt_text = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural= '01. Banners'

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" height="40" />' % (self.img.url))

    def __str__(self):
        return self.alt_text




# Category
class Category(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="cat_imgs/")

    class Meta:
        verbose_name_plural= '02. Categories'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))
    
    def __str__(self):
        return self.title
    


# Brand
class Brand(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="brand_imgs/")

    class Meta:
        verbose_name_plural= '03. Brands'

    def __str__(self):
        return self.title
    



# Color
class Color(models.Model):
    title = models.CharField(max_length=250)
    color_code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural= '04. Colors'

    def color_bg(self):
        return mark_safe('<div style="width:30px; height:30px; background:%s;"><div/>' % (self.color_code))

    def __str__(self):
        return self.title
    




# Size
class Size(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural= '05. Sizes'

    def __str__(self):
        return self.title
    




# Product Model 
class Product(models.Model):
    title       = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=200)
    detail      = models.TextField()
    specs       = models.TextField()
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand       = models.ForeignKey(Brand, on_delete=models.CASCADE)
    status      = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural= '06. Products'

    def __str__(self):
        return self.title
    


# Product Attribute
class ProductAttribute(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    color       = models.ForeignKey(Color, on_delete=models.CASCADE)
    size        = models.ForeignKey(Size, on_delete=models.CASCADE)
    price       = models.PositiveIntegerField()
    image       = models.ImageField(upload_to="product_imgs/", null=True)

    class Meta:
        verbose_name_plural= '07. ProductAttributes'

    def image_tag(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.product.title    
    





# Order 
status_choice = (
    ('process', 'In Process'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)
class CartOrder(models.Model):
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amt    = models.FloatField()
    paid_status  = models.BooleanField(default=False)
    order_dt     = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(choices=status_choice, default= 'process', max_length=150)

    class Meta:
        verbose_name_plural= '08. Orders'


# Order Items
class CartOrderItems(models.Model):
    order       = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no  = models.CharField(max_length=150)
    item        = models.CharField(max_length=150)
    image       = models.CharField(max_length=200)
    qty         = models.IntegerField()
    price       = models.FloatField()
    total       = models.FloatField()

    class Meta:
        verbose_name_plural= '09. Order Items'

    def image_tag(self):
        return mark_safe('<img src="/media/%s" width="50" height="50" />' % (self.image))
    





# Product Review
RATING = (
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)
class ProductReview(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_text   = models.TextField()
    review_rating = models.CharField(choices=RATING, max_length=150)

    class Meta:
        verbose_name_plural= '10    . Reviews'

    def get_review_rating(self):
        return self





# WhishList
class WhishList(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    product       = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural= '11    .Wishlist'



# AddressBook
class UserAddressBook(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile        = models.CharField(max_length=50, null=True)
    address       = models.TextField()
    status        = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural= '12. AddressBook'