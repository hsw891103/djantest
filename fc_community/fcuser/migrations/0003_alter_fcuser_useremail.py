# Generated by Django 4.0.4 on 2022-06-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0002_fcuser_useremail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fcuser',
            name='useremail',
            field=models.EmailField(max_length=128, null=True, verbose_name='사용자이메일'),
        ),
    ]