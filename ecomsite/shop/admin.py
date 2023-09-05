from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    def set_is_deleted_to_true(modeladmin, request, queryset):
        queryset.update(is_deleted=True)
    set_is_deleted_to_true.short_description = "Set is_deleted to True"

    def set_is_deleted_to_false(modeladmin, request, queryset):
        queryset.update(is_deleted=False)
    set_is_deleted_to_false.short_description = "Set is_deleted to False"

    list_display = ['title', 'price', 'discount_price','category','image',"is_deleted"]
    search_fields = ['title','category']
    actions = [set_is_deleted_to_true, set_is_deleted_to_false]

admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['items','name','address','city']

admin.site.register(Order,OrderAdmin)    