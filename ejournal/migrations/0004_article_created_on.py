# Generated by Django 3.2.8 on 2022-01-03 05:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ejournal', '0003_alter_article_title_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
