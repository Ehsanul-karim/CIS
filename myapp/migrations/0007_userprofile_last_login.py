# Generated by Django 4.2.6 on 2023-11-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_userprofile_nid_alter_userprofile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='last_login',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
