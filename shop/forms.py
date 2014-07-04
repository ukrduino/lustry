# -*- coding: utf-8 -*-
from django.forms import ModelForm
from shop.models import Comment, Order
from captcha.fields import CaptchaField


class CommentForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['comment_text']


class OrderForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Order
        exclude = ['order_date',
                   'order_confirmed',
                   'order_delivered',
                   'order_products',
                   'order_code',
                   'order_summ']
