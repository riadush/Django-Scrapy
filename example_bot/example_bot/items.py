# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from app.models import ExampleDotCom


class ExampleDotComItem(DjangoItem):
    django_model = ExampleDotCom