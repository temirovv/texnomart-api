# Generated by Django 5.1.6 on 2025-03-14 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Kategoriya rasmi', upload_to='categories/')),
                ('name', models.CharField(max_length=255)),
                ('parent', models.ForeignKey(help_text='Kategoriya otasi', on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Mahsulot nomi', max_length=255)),
                ('price', models.FloatField(help_text='Mahsulot narxi')),
                ('installment_payment_12', models.FloatField(help_text="12 oyda davomida qancha summadan to'lashi")),
                ('installment_payment_24', models.FloatField(help_text="24 oyda davomida qancha summadan to'lashi")),
                ('attributes', models.JSONField(help_text='Mahsulot tavfsilotlari')),
                ('category', models.ForeignKey(help_text='Mahsulot kategoriyasi', on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Mahsulot rasmi', upload_to='product-images/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Banner rasmi', upload_to='promotions/')),
                ('title', models.CharField(help_text='Aksiya sarlavhasi', max_length=255)),
                ('description', models.TextField(help_text='Aksiya tavfsilotlari')),
                ('is_active', models.BooleanField(default=True, help_text='Aksiya aktivligi')),
                ('start', models.DateField(help_text='Aksiya boshlanish sanasi')),
                ('end', models.DateField(help_text='Aksiya tugash sanasi')),
                ('products', models.ManyToManyField(through='store.ProductInPromotion', to='store.product')),
            ],
        ),
        migrations.AddField(
            model_name='productinpromotion',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.promotion'),
        ),
    ]
