# Generated by Django 4.2.3 on 2023-07-29 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchmate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
    ]