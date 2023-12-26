from django.contrib import admin
from testApp.models import products,user_cred,card,address
admin.site.register(products)
admin.site.register(user_cred)
admin.site.register(card)
admin.site.register(address)

# Register your models here.
# from .models import Product

# admin.site.register(Product)