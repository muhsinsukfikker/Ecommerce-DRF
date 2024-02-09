from django.contrib import admin
from api.models import Category,Product,Basket,BasketItem

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketItem)