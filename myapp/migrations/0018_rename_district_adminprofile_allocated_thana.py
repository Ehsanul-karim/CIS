# Generated by Django 4.2.6 on 2023-11-08 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_districtnames_alter_adminprofile_district'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminprofile',
            old_name='District',
            new_name='Allocated_Thana',
        ),
    ]
