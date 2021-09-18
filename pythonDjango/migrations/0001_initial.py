# Generated by Django 3.2.7 on 2021-09-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=18)),
                ('Name', models.CharField(max_length=150)),
                ('Address', models.TextField(max_length=500)),
                ('Product', models.CharField(max_length=5)),
                ('Date', models.DateField()),
            ],
        ),
    ]