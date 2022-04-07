# Generated by Django 3.1.14 on 2022-04-07 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=255, verbose_name='E-Mail')),
                ('message', models.CharField(default='', max_length=2000, verbose_name='Wiadomość')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data')),
            ],
        ),
    ]
