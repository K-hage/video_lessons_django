from django.contrib import admin

from products.models import Product, AccessProduct

admin.site.register(Product, admin.ModelAdmin)
admin.site.register(AccessProduct, admin.ModelAdmin)
