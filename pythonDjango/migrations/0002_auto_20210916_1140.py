# Generated by Django 3.2.7 on 2021-09-16 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Product',
            new_name='product',
        ),
    ]