from django.contrib import admin
from .models import Category,Product

# Register your models here.
# admin.site.register(food_items)
# admin.site.register(food_juices)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Product,ProductAdmin)
