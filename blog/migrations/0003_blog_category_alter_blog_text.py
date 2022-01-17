# Generated by Django 4.0.1 on 2022-01-14 15:18

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
