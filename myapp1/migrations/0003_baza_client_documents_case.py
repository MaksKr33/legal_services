# Generated by Django 3.2.15 on 2022-10-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_remove_baza_client_documents_case'),
    ]

    operations = [
        migrations.AddField(
            model_name='baza_client',
            name='documents_case',
            field=models.FileField(null=True, upload_to='DownloadFile/%Y/%m/%d/', verbose_name='Загрузка документів'),
        ),
    ]
