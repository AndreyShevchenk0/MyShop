from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
User = get_user_model()


class Product(models.Model):
    """ Модель продукта """

    #user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    #kanban1 = models.ForeignKey(Kontakt, blank=False, on_delete=models.CASCADE, verbose_name='наследование конт.')
    name_product = models.CharField(max_length=100, verbose_name='товар')
    price = models.IntegerField(default=0, verbose_name='цена')
    added_product = models.DateTimeField(auto_now_add=True)
    update_product = models.DateTimeField(auto_now=True)
    discount = models.IntegerField(default=0, verbose_name='скидка')

    def __str__(self):
        return self.name_product
        #return self.price / discount

    class Meta:
        verbose_name_plural = 'Товари'
        verbose_name = 'Товар'


class deal(models.Model):
    """ Cтадии - Продажи товара """

    CATEGORY = [
        ('ожидание', 'Ожидание'),
        ('виполнен', 'Виполнен'),
        ('оплачен', 'Оплачен'),
    ]

    time = models.DateTimeField(auto_now_add=True,)
    #kanban = models.ForeignKey(Kontakt, on_delete=models.CASCADE, verbose_name='имя заказчика')
    statu = models.CharField(max_length=10, choices=CATEGORY, default='Ожидание', verbose_name='статус заказа')
    #gods = models.ForeignKey(goods, on_delete=models.CASCADE, verbose_name=' список товара покупателя')

    class Meta:
        verbose_name_plural = 'Статус Заказов'
        verbose_name = 'Статус Заказа'

    def __str__(self):
        return self.statu


class sales_consultant(models.Model):
    """ Продавец консультант """

    CATEGORY = [
        ('ожидание', 'Ожидание'),
        ('виполнен', 'Виполнен'),
    ]

    kanban1 = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE, verbose_name='товар')
    status = models.CharField(max_length=10, choices=CATEGORY, default='Ожидание', verbose_name='статус заказа')

    def __str__(self):
        return self.status


class cashier(models.Model):
    """ Касир """

    CATEGORY = [
        ('ожидание', 'Ожидание'),
        ('оплачен', 'Оплачен'),
    ]

    kanban2 = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE, verbose_name='товар')
    stat = models.CharField(max_length=10, choices=CATEGORY, default='Ожидание', verbose_name='статус заказа')

    def __str__(self):
        return self.stat


class accountant(models.Model):
    """ Бухгалтер """

    kanban3 = models.ForeignKey(Product, blank=False, on_delete=models.CASCADE, verbose_name='товар')
    kanban4 = models.ForeignKey(deal, blank=False, on_delete=models.CASCADE, verbose_name='статус')
    #kanban5 = models.ManyToManyField(Product, blank=False, verbose_name='товар+')
    #kanban6 = models.ManyToManyField(deal, blank=False, verbose_name='статус+')

    # def __str__(self):
    #     return self.name_product
