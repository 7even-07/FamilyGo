# Generated by Django 4.2.7 on 2024-01-03 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('familygo', '0013_cart_tcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shirt',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='familygo.shirts_product'),
        ),
    ]
