# Generated by Django 2.2.6 on 2019-10-14 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content_a', models.CharField(max_length=100)),
                ('content_b', models.CharField(max_length=100)),
            ],
        ),
    ]