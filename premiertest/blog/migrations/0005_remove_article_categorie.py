# Generated by Django 2.2 on 2019-05-06 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='categorie',
        ),
    ]