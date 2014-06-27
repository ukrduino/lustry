# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
# маленький и клевенький ClassBasedView!!!

from django.views.generic import TemplateView, ListView
from shop.models import Lustra  # импортируем модели



urlpatterns = patterns('',
    # если просто набрать адрес сайта например
    # http://127.0.0.1:8000/ то сработает функция products в файле views в папке(приложении) Shop
    url(r'^$', TemplateView.as_view(template_name="main.html"), name="home"),
        # маленький и клевенький ClassBasedView!!!
    url(r'^lustry/$', ListView.as_view(model = Lustra, template_name = "lustra_list.html"), name='lustra_list'),
        # маленький и клевенький ClassBasedView!!!
    url(r'^lustry/(?P<product_id>\d+)$', 'shop.views.lustra_detail', name='lustra_detail'),
    #url(r'^lustry/(?P<pk>\d+)$', DetailView.as_view(model = Lustra, template_name = "lustra_detail.html"), name='lustra_detail'),
        # маленький и клевенький ClassBasedView!!!
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name="about"),

#    url(r'^product/add_like/(?P<product_id>\d+)$', 'Shop.views.add_like', name='like'),
    url(r'^lustry/add_comment/(?P<product_id>\d+)$', 'shop.views.add_comment', name='comment'),





    # покупка товаров
    url(r'^add_product/(?P<product_id>\d+)$', 'shop.views.add_to_cart_main', name='add_main'),
    url(r'^cart/add_product/(?P<product_id>\d+)$', 'shop.views.add_to_cart', name='add'),
    url(r'^cart/rem_product/(?P<product_id>\d+)$', 'shop.views.rem_from_cart', name='rem'),
    url(r'^cart/cart$', 'shop.views.cart', name='my_cart'),
    url(r'^cart/cart/make_order$', 'shop.views.make_order', name='make_order'),
)