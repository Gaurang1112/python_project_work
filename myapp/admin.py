from django.contrib import admin
from .models import User,Contact,Product,Wishlist,Cart
# Register your models here.
admin.site.site_header = "Karma-Shoes"
admin.site.register(User)
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Wishlist)
admin.site.register(Cart)