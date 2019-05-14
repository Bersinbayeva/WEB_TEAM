from django.contrib import admin
from .models import Category, Sections, Product, Basket


admin.site.register(Sections)
admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')