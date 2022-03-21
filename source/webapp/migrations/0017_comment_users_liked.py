# Generated by Django 4.0 on 2022-03-21 11:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0016_remove_article_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='users_liked',
            field=models.ManyToManyField(related_name='comments_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]