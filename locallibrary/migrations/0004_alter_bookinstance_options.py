# Generated by Django 4.2 on 2023-08-26 03:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locallibrary', '0003_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'set book as returned'),)},
        ),
    ]