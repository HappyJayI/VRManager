# Generated by Django 2.0 on 2018-01-12 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('VRMApp', '0002_auto_20180112_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmpWorkPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WorkDate', models.DateField(verbose_name='근무일')),
                ('StrDate', models.DateField(verbose_name='시작일')),
                ('StrTime', models.TimeField(blank=True, null=True, verbose_name='시작시간')),
                ('EndDate', models.DateField(verbose_name='종료일')),
                ('EndTime', models.TimeField(blank=True, null=True, verbose_name='종료시간')),
                ('WorkTime', models.FloatField(blank=True, null=True, verbose_name='계산근무시간')),
                ('AppWorkTime', models.FloatField(blank=True, null=True, verbose_name='확정근무시간')),
                ('Activity', models.CharField(blank=True, max_length=20, null=True, verbose_name='활동내역')),
                ('Remark', models.CharField(blank=True, max_length=20, null=True, verbose_name='비고')),
                ('RegDT', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='등록일시')),
                ('UptDT', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='수정일시')),
                ('EmpSeq', models.ForeignKey(db_column='EmpSeq', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='VRMApp.Emp', verbose_name='사원')),
                ('RegUserSeq', models.ForeignKey(db_column='RegUserSeq', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='등록자')),
                ('UptUserSeq', models.ForeignKey(db_column='UptUserSeq', editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='수정자')),
            ],
            options={
                'verbose_name': '입출고',
                'verbose_name_plural': '입출고',
            },
        ),
    ]
