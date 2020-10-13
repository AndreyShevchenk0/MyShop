from django.contrib import admin
from .models import Product, deal, sales_consultant, cashier, accountant
from math import ceil


admin.site.register(Product)

admin.site.register(deal)

admin.site.register(sales_consultant)

admin.site.register(cashier)

admin.site.register(accountant)

#@admin.register(deal)
class BbAdmin(admin.ModelAdmin):
    list_display = ('status', 'stat', 'statu', 'gods', 'kanban1', 'kanban2', 'kanban3', 'time', 'price',
                    'added_product', 'update_product')
    #list_display_links = ('status', 'gods', 'time', 'price')
    search_fields = ('status', 'gods', 'time', 'price')

    # def discount_20(self, request, queryset):
    #     from math import ceil
    #     discount = 20  # percentage
    #
    #     for product in queryset:
    #         """ Set a discount of 20% to selected products """
    #         multiplier = discount / 100.  # discount / 100 in python 3
    #         old_price = product.price
    #         new_price = ceil(old_price - (old_price * multiplier))
    #         product.price = new_price
    #         product.save(update_fields=['price'])
    #
    # discount_20.short_description = 'Set 20%% discount'
