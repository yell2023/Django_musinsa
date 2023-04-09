# Generated by Django 4.2 on 2023-04-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_rename_invetory_inventory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inbound',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='outbound',
            old_name='product_id',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='total_inbound_amount',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='total_inbound_quantity',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='total_outbound_amount',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='total_outbound_quantity',
        ),
        migrations.AddField(
            model_name='inbound',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='outbound',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]