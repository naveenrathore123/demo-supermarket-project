# Generated by Django 3.2.6 on 2021-12-16 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supermarket_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='supermarket_api.category'),
            preserve_default=False,
        ),
    ]
