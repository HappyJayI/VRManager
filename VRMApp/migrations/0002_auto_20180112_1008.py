# Generated by Django 2.0 on 2018-01-12 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRMApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contents',
            name='ContentsName',
            field=models.CharField(max_length=20, unique=True, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='ContentsNo',
            field=models.CharField(max_length=20, unique=True, verbose_name='영화번호'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='ContentsSeq',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='영화내부코드'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='Director',
            field=models.CharField(max_length=20, unique=True, verbose_name='감독'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='FileName',
            field=models.CharField(max_length=50, unique=True, verbose_name='파일명'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='MainActors',
            field=models.CharField(max_length=20, unique=True, verbose_name='주연배우'),
        ),
        migrations.AlterField(
            model_name='contents',
            name='RegNo',
            field=models.CharField(max_length=20, unique=True, verbose_name='영등위등록번호'),
        ),
    ]
