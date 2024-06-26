# Generated by Django 5.0.4 on 2024-06-05 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0010_remove_service_category_remove_service_generals_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ManyToManyField(to='root.category'),
        ),
        migrations.AddField(
            model_name='service',
            name='general',
            field=models.ManyToManyField(to='root.option'),
        ),
    ]
