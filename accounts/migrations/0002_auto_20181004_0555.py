# Generated by Django 2.1.1 on 2018-10-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='users/no_avatar.jpg', upload_to='users/%Y/%m/%d/'),
        ),
    ]
