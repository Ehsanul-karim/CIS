# Generated by Django 4.2.6 on 2023-11-02 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_userprofile_registerip'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='registerLocation',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
