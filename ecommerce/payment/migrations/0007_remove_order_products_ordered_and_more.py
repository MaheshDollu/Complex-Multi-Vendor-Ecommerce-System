# Generated by Django 4.1.2 on 2022-10-30 21:56

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("payment", "0006_alter_orderitem_order_alter_orderitem_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="products_ordered",
        ),
        migrations.RemoveField(
            model_name="order",
            name="total_quantity",
        ),
    ]
