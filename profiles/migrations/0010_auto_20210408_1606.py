# Generated by Django 3.1.7 on 2021-04-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_remove_post_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='imagefile',
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='imagefile', max_length=500),
        ),
    ]
