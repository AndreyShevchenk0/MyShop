from django.contrib import admin
from .models import Product, deal, sales_consultant, cashier, accountant
from math import ceil


admin.site.register(deal)

admin.site.register(sales_consultant)

admin.site.register(cashier)

@admin.register(accountant)
class AccountantAdmin(admin.ModelAdmin):
    list_display = ['kanban3', 'kanban4']
    search_fields = ['kanban3', 'kanban4']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    actions = ['discount_20']
    list_display = ['name_product', 'price', 'added_product', 'update_product']
    list_filter = ['price', 'added_product', 'update_product']

    def discount_20(self, request, queryset):
        from math import ceil
        discount = 20

        for product in queryset:
            """ фильтр уменьшаюший стоимость продукта на 20% """
            multiplier = discount / 100.
            old_price = product.price
            new_price = ceil(old_price - (old_price * multiplier))
            product.price = new_price
            product.save(update_fields=['price'])

    discount_20.short_description = 'скидка 20%%'