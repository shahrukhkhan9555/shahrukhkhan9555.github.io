# Generated by Django 2.2.4 on 2019-08-20 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=24),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(default='03214659359', max_length=15),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='Shahrukh', editable=False, max_length=8),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Khan', editable=False, max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(default='Software Engineer', editable=False, max_length=20),
        ),
    ]