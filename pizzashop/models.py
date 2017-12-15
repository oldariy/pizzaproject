from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя', blank=True)
    last_name = models.CharField(max_length=50, verbose_name='Фамилия', blank=True)
    address = models.CharField(max_length=150, verbose_name='Адес', blank=True)
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(blank=True, verbose_name='Email')

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Item(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    description = models.TextField(max_length=300, verbose_name='Описание', blank=True)
    price = models.PositiveSmallIntegerField(default=0, verbose_name='Цена')
    image = models.ImageField(upload_to='pizzashop/', blank=True, verbose_name='Изображение', default='')

    def image_tag(self):
        return u'<img  src="%s"/>' % self.image.url
    image_tag.short_description = 'Изображение'
    image_tag.allow_tags = True

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', verbose_name='Клиент')
    items = models.ManyToManyField(Item, through='OrderItem', verbose_name='Товары')

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
    status = models.CharField(max_length=3, choices=STATUS, default=CREATED, verbose_name='Статус заказа')

    def __str__(self):
        return str(self.customer) + ' : ' + str(self.status)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    item = models.ForeignKey(Item, verbose_name='Товар')
    order = models.ForeignKey(Order, verbose_name='Номер заказа')
    count = models.PositiveSmallIntegerField(default=1, verbose_name='Количество')
    price_per_item = models.PositiveSmallIntegerField(default=0, verbose_name='Цена')
    total_price = models.PositiveSmallIntegerField(default=0, verbose_name='Сумма заказа')
    is_active = models.BooleanField(default=True, verbose_name='Готовность')
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Создан')
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name='Обновлен')

    def __str__(self):
        return str(self.item) + ' : ' + str(self.order)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'


class BasketItem(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    item = models.ForeignKey(Item)
    order = models.ForeignKey(Order, blank=True, null=True)
    count = models.PositiveSmallIntegerField(default=1)
    price_per_item = models.PositiveSmallIntegerField(default=0)
    total_price = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.item) + ' : ' + str(self.order)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        price_per_item = self.item.price
        self.price_per_item = price_per_item
        self.total_price = int(self.count) * price_per_item
        super(BasketItem, self).save(*args, **kwargs)
