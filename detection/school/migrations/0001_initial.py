# Generated by Django 2.0.2 on 2018-05-17 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='S_CURRICULUM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('week_day', models.IntegerField(default=0)),
                ('time_begin', models.TimeField()),
                ('time_end', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('s_class', models.IntegerField(default=0)),
                ('s_id', models.CharField(max_length=200)),
                ('s_grade', models.CharField(max_length=100)),
                ('s_photo', models.ImageField(upload_to='cover/%Y/%m/%d/')),
                ('s_time', models.DateField(auto_now_add=True)),
                ('s_curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.S_CURRICULUM')),
            ],
        ),
    ]