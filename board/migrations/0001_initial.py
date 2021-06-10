# Generated by Django 3.2.4 on 2021-06-09 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('comment', models.TextField(max_length=300)),
                ('createDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
