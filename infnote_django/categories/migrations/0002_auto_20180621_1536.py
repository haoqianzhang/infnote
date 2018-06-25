# Generated by Django 2.0.6 on 2018-06-21 15:36

from django.db import migrations


def initial_categories(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    Category.objects.create(name='/', display_name='general', desc='General category for any kind of topics.')
    Category.objects.create(name='/fb', display_name='feedback', desc='Report bugs here.')
    Category.objects.create(name='/bitcoin', display_name='bitcoin', desc='Make discussions of bitcoin.')


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_categories),
    ]
