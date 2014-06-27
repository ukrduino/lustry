# -*- coding: utf-8 -*-
from django.db import models
# импортируем random  для функции make_upload_path
import random
# импортируем модель пользователя
# http://arunrocks.com/building-a-hacker-news-clone-in-django-part-1/
# from django.contrib.auth.models import User
from django.utils import timezone


# функция Переопределение имени загружаемого файла.
def make_upload_path(instance, filename, prefix = False):
    n1 = random.randint(0, 10000)
    n2 = random.randint(0, 10000)
    n3 = random.randint(0, 10000)
    filename = str(n1)+"_"+str(n2)+"_"+str(n3) + '.jpg'
    return u"%s/%s" % ('static', filename)  # и кладет в папку указ. в "settings" в "IMAGE_UPLOAD_DIR"


class Product(models.Model):
    class Meta:
        abstract = True

    product_title = models.CharField(max_length=100, verbose_name='Название товара', blank=False, unique=True)
    product_slug = models.CharField(max_length=100, verbose_name='URL')
    product_text = models.TextField(verbose_name='Описание товара', blank=False)
    product_date = models.DateTimeField(verbose_name='Дата размещения', blank=False)
    product_date_change = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    product_date_change.editable = True  # для того, чтобы в админке отобр поле даты если в нем стоит "auto_now=True"
    product_likes = models.IntegerField(default=0, verbose_name='Лайки')
    product_image = models.ImageField(upload_to=make_upload_path, default="", verbose_name='Изображение')
    product_sold = models.IntegerField(default=0, verbose_name='Продано штук')
    product_start_price = models.IntegerField(verbose_name='Начальная цена', default=0)
    product_current_price = models.IntegerField(verbose_name='Текущая цена', default=0)
    product_present = models.BooleanField(verbose_name='В наличии', default=True)
    product_order = models.BooleanField(verbose_name='Под заказ', default=False)

# при обращении к классу Product возвращает его имя - product_title
    def __unicode__(self):
        return self.product_title

# функция формирования пути к картинке объекта Product для отображения в админке
    def pic(self):
        if self.product_image:  # как заменять адрес сайта ???
            return '<img src="http://lustry.pythonanywhere.com/%s", height="100"/>' % self.product_image.url
        else:
            return '(none)'
    pic.short_description = 'Изображение'
    pic.allow_tags = True


class Lustra(Product):
    P1 = "Е27"
    P2 = "E14"
    P3 = "G4"
    P4 = "G5.3"
    P5 = "G9"
    P6 = "GU10"
    P7 = "MR16"
    P8 = "MR11"

    P_CHOISES = ((P1, "E27"), (P2, "E14"), (P3, "G4"), (P4, "G5.3"),
                (P5, "G9"), (P6, "GU10"), (P7, "MR16"), (P8, "MR11"),)

    class Meta():
        db_table = 'lustra'  # определяем свое название таблицы в Б.Д.
        verbose_name = 'Люстра'  # имя модели в админке в ед ч
        verbose_name_plural = 'Люстры'  # имя модели в админке в мн ч
    product_lusta_h = models.IntegerField(verbose_name='Высота', blank=False)
    product_lusta_w = models.IntegerField(verbose_name='Ширина', blank=False)
    product_lusta_patr = models.CharField(max_length=5, verbose_name='Тип патрона', choices=P_CHOISES)
    product_lusta_lamps = models.IntegerField(verbose_name='Количество ламп', blank=False)
    product_lusta_l_power = models.IntegerField(verbose_name='Мощьность лампы', blank=False)
    product_lusta_arm_col = models.CharField(max_length=50, verbose_name='Цвет арматуры', blank=False)
    product_lusta_arm_mat = models.CharField(max_length=50, verbose_name='Материал арматуры', blank=False)
    product_lusta_plaf_col = models.CharField(max_length=50, verbose_name='Цвет плафонов', blank=False)
    product_lusta_plaf_mat = models.CharField(max_length=50, verbose_name='Материал плафонов', blank=False)
    product_lusta_prod = models.CharField(max_length=50, verbose_name='Производитель', blank=False)
    product_lusta_country = models.CharField(max_length=50, verbose_name='Страна', blank=False)
    product_lusta_compl = models.BooleanField(verbose_name='Лампы в комплекте', default=False)


class Comment(models.Model):  # TODO добавить пользователя написавшего комментарий
    class Meta():
        db_table = 'comment'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    comment_text = models.TextField(max_length=1000, verbose_name='Текст комментария')
    comment_date = models.DateTimeField(verbose_name='Дата комментария', auto_now=True,)
    comment_date.editable = True  # для того, чтобы в админке отображалось поле даты если в нем стоит "auto_now=True"
    comment_product = models.ForeignKey(Lustra)  # связка с моделью Lustra


class Order(models.Model):
    P1 = "Пр-опл"
    P2 = "Нал-плат"
    P3 = "Опл-кур"
    P4 = "Опл-маг"
    D1 = "Сам"
    D2 = "НП"
    D3 = "Кур"

    PAY_CHOISES = ((P1, "Предоплата"), (P2, "Наложный платеж"), (P3, "Оплата курьеру"), (P4, "Оплата в магазине"),)
    DELIV_CHOISES = ((D1, "Самовывоз из магазина"), (D2, "Новая Почта"), (D3, "Доставка курьером"),)

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    order_person = models.CharField(max_length=100, verbose_name='Фамилия Имя Отчество покупателя', blank=False)
    order_person_phone = models.CharField(max_length=30, verbose_name='Контактный телефон', blank=False)
    order_person_address = models.CharField(max_length=100, verbose_name='Адрес доставки', blank=False)
    order_person_email = models.EmailField(max_length=100, verbose_name='E-mail', blank=False)
    order_pay_option = models.CharField(max_length=30, verbose_name='Тип оплаты', blank=False, choices=PAY_CHOISES)
    order_delivery_option = models.CharField(max_length=30, verbose_name='Тип доставки',
                                             blank=False, choices=DELIV_CHOISES)
    order_date = models.DateTimeField(verbose_name='Дата размещения', default=timezone.now)
    order_delivered = models.BooleanField(verbose_name='Заказ выполнен', default=False)
    order_products = models.CharField(max_length=200, verbose_name='Заказанные товары', blank=True)
    order_code = models.CharField(max_length=4, verbose_name='Код заказа', default=random.randint(0, 10000))
    order_password = models.CharField(max_length=15, verbose_name='Пароль к заказу')
    order_summ = models.IntegerField(max_length=4, verbose_name='Сумма заказа', default=0)

# при обращении к классу Product возвращает его имя - product_title
    def __unicode__(self):
        return self.order_code







# Использование south
# python manage.py schemamigration shop --initial
# Above step creates migration folder as default.
# python manage.py migrate shop --fake
# generates a fake migration.
# python manage.py schemamigration shop --auto
# Then you can add fields as you wish and perform the above command.
# python manage.py migrate shop
