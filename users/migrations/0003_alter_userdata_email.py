# Generated by Django 3.2.4 on 2021-06-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userdata_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='email',
            field=models.EmailField(default='none@example.com', max_length=254),
        ),
    ]
