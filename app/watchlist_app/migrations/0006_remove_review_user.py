# Generated by Django 4.0.6 on 2022-07-25 02:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0005_review_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
    ]
