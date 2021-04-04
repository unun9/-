from django.contrib import admin

# Register your models here.
from app_app_1.models import Product,Review,Cotegory

admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Cotegory)
