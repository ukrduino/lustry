# -*- coding: utf-8 -*-
from django.contrib import admin
from shop.models import * # импортируем модели

# "Связывающий" класс  - добавляет в админку одного класса другой класс например в админке класса Product
# будут видны и комментарии к нему (класс Comment)
class ProductInline(admin.TabularInline):
    model = Comment  # добавляем комментарии
    extra = 1  # сколько? - один комментарий


class ProductAdmin(admin.ModelAdmin):  # класс для перенастройки отображения класса Product в админке
    prepopulated_fields = {'product_slug': ('product_title',)}  # из поля product_title транслитом заполняется
                                                                # поле product_slug
    # какие поля показывать в админке Product
#    fields = ['product_date', 'product_title', 'product_slug', 'product_text',
#              'product_image', 'product_start_price', 'product_current_price', 'product_present', 'product_order']
    inlines = [ProductInline]  # присоединяем "Связывающий" класс
    list_display = ['product_title', 'product_date', 'product_date_change', 'product_start_price', 'product_current_price',
                    'product_present', 'pic']  # возможность просматривать записи
                                                                                    # Product в виде таблицы
    list_filter = ['product_date', 'product_date_change', 'product_present']  # включение фильтра по датам
    search_fields = ['product_title']
#    filter_horizontal = ('product_category_MTM',)  # Позволяет управлять  категориями в товаре
                                                   # (добавлять, удалять, менять)

class OrderAdmin(admin.ModelAdmin):  # класс для перенастройки отображения класса Product в админке

    list_display = ['order_code', 'order_person', 'order_date', 'order_summ', 'order_delivered',
                    'order_confirmed']  # возможность просматривать записи
                                        # Order в виде таблицы
    list_filter = ['order_date', 'order_summ', 'order_delivered', 'order_confirmed']  # включение фильтра по датам
    search_fields = ['order_code', 'order_person']

# Register your models here.
admin.site.register(Lustra, ProductAdmin)  # регистрация класса Product в админке с указанием, что вместо
                                           # него будут настройки описанные в ProductAdmin
admin.site.register(Order, OrderAdmin)  # регистрация класса Order в админке
