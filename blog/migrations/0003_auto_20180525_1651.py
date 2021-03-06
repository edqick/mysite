# Generated by Django 2.0 on 2018-05-25 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180525_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blog_author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.BlogType', verbose_name='分类'),
        ),
    ]
