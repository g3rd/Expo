# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from decimal import Decimal

from django.db import models, migrations

def raise_price(apps, schema_editor):
    Pizza = apps.get_model("pizza", "Pizza")
    for pizza in Pizza.objects.all():
        pizza.price = pizza.price + pizza.price * Decimal(0.1)
        pizza.save()

def lower_price(apps, schema_editor):
    Pizza = apps.get_model("pizza", "Pizza")
    for pizza in Pizza.objects.all():
        pizza.price = pizza.price * Decimal(0.90909)
        pizza.save()

class Migration(migrations.Migration):
    dependencies = [
        ('pizza', '0002_pizza_price'),
    ]
    operations = [
        migrations.RunPython(raise_price, reverse_code=lower_price),
    ]
