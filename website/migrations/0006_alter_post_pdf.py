# Generated by Django 4.2.3 on 2023-09-26 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_alter_post_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pdf',
            field=models.FileField(null=True, upload_to='pdf/'),
        ),
    ]
