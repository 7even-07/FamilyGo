# Generated by Django 4.2.7 on 2024-01-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familygo', '0010_otherproductcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount', models.CharField(max_length=30)),
                ('payment_id', models.CharField(max_length=30)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='OtherProductCategory',
        ),
    ]
