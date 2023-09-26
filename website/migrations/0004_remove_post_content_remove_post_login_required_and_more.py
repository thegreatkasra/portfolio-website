# Generated by Django 4.2.3 on 2023-09-26 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='login_required',
        ),
        migrations.AddField(
            model_name='post',
            name='pdf',
            field=models.FilePathField(null=True),
        ),
    ]
