from operator import mod
from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=100, help_text='Введите имя покупателя', verbose_name='Покупатель', null=False)
    content = models.TextField(help_text='Введите содержание заказа', verbose_name='Содержание заказа', null=True, blank=True)
    cost = models.FloatField(help_text='Введите общую стоимость', verbose_name='Общая стоимость', null=False)
    date_order = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.cost}руб {self.date_order.strftime("%d.%m.%y %H:%M")}'


class Product(models.Model):
    title = models.CharField(max_length=100, help_text='Введите наименование товара', verbose_name='Товар', null=False)
    price = models.FloatField(help_text='Введите стоимость', verbose_name='Цена', null=False)

    def __str__(self):
        return self.title


