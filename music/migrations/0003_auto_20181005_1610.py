# Generated by Django 2.1.1 on 2018-10-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='image',
            field=models.FileField(upload_to=''),
        ),
    ]