# Generated by Django 3.2 on 2021-04-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotation', '0006_auto_20210425_1705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='agree',
        ),
        migrations.RemoveField(
            model_name='line',
            name='total_agree',
        ),
        migrations.RemoveField(
            model_name='line',
            name='total_disagree',
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='line',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
