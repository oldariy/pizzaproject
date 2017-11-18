from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    phone = PhoneNumberField()
    email = models.EmailField(blank=True)


class Item(models.Model):
    title = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField(default=0)


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders')
    items = models.ManyToManyField(Item, through='OrderItem')

    CREATED = 'CR'
    NOT_CONFIRMED = 'NCF'
    CONFIRMED = 'CF'
    CANCELED_BY_CUSTOMER = 'CBC'
    CANCELED_BY_OPERATOR = 'CBO'
    COMPLETED = 'CM'
    FAILED = 'FL'
    STATUS = (
        (CREATED, 'Создан'),
        (NOT_CONFIRMED, 'Не подтвержден'),
        (CONFIRMED, 'Подтвержден'),
        (CANCELED_BY_CUSTOMER, 'Отменен заказчиком'),
        (CANCELED_BY_OPERATOR, 'Отклонен оператором'),
        (COMPLETED, 'Выполнен'),
        (FAILED, 'Провален'),
    )
    status = models.CharField(max_length=3, choices=STATUS, default=CREATED)


class OrderItem(models.Model):
    item = models.ForeignKey(Item)
    order = models.ForeignKey(Order)
    count = models.PositiveSmallIntegerField()
