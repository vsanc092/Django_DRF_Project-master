from django.contrib import admin
from .models import Comment, Good, Category

admin.site.register(Comment)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock_availability']
    list_filter = ['stock_availability']
    list_editable = ['price', 'stock_availability']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Good, ProductAdmin)
