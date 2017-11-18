from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Customer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя', blank=True)
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', blank=True)
    address = models.CharField(max_length=150, verbose_name='Адес')
    phone = PhoneNumberField(verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Email')

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Item(models.Model):
    title = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField(default=0)
    image = models.ImageField(upload_to='pizzashop/', blank=False, verbose_name='Логотип', default='')


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
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
