# Generated by Django 2.0 on 2018-01-12 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRMApp', '0005_auto_20180112_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='ContentsNo',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='영화번호'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='Director',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='감독'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='FileName',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='파일명'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='MainActors',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='주연배우'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='RegNo',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='영등위등록번호'),
        ),
    ]
