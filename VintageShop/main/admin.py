from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Brand)
admin.site.register(Size)



class ProductAdmin(admin.ModelAdmin):
    list_display  = ('id', 'title', 'category', 'brand', 'status', 'is_featured')
    list_editable = ('status', 'is_featured')

admin.site.register(Product, ProductAdmin)




class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('title', 'image_tag')

admin.site.register(Category, CategoryAdmin)




class BannerAdmin(admin.ModelAdmin):
    list_display  = ('alt_text', 'image_tag')

admin.site.register(Banner, BannerAdmin)




class ColorAdmin(admin.ModelAdmin):
    list_display  = ('title', 'color_bg')

admin.site.register(Color, ColorAdmin)




# Product Attribute
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display  = ('id', 'image_tag', 'product', 'price', 'color', 'size')

admin.site.register(ProductAttribute, ProductAttributeAdmin)





# Order 
class CartOrderAdmin(admin.ModelAdmin):
    list_editable = ('paid_status', 'order_status')
    list_display  = ('user', 'total_amt', 'paid_status', 'order_dt', 'order_status')

admin.site.register(CartOrder, CartOrderAdmin)




# Order 
class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display  = ('order', 'invoice_no', 'item', 'image_tag', 'qty', 'price', 'total')

admin.site.register(CartOrderItems, CartOrderItemsAdmin)




# Order 
class ProductReviewAdmin(admin.ModelAdmin):
    list_display  = ('user', 'product', 'review_text', 'get_review_rating')

admin.site.register(ProductReview, ProductReviewAdmin)





# WhishList
class WhishListAdmin(admin.ModelAdmin):
    list_display  = ('user', 'product')

admin.site.register(WhishList, WhishListAdmin)





# WhishList
class UserAddressBookAdmin(admin.ModelAdmin):
    list_display  = ('user', 'address', 'status')

admin.site.register(UserAddressBook, UserAddressBookAdmin)