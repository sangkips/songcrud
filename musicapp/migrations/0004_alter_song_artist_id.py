# Generated by Django 4.1.2 on 2022-10-09 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_song_artist_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicapp.artist'),
        ),
    ]
