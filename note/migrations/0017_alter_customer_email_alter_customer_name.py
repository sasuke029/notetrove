# Generated by Django 4.1.4 on 2023-09-24 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0016_room_digital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]