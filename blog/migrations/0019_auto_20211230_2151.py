# Generated by Django 3.2.8 on 2021-12-30 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0018_alter_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='date_created',
            new_name='created_on',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='comment',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='subject',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]