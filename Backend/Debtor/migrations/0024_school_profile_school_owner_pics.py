# Generated by Django 4.0.5 on 2022-08-12 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Debtor', '0023_school_founded_school_number_of_students_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='school_profile',
            name='School_owner_pics',
            field=models.ImageField(default='fixed.jpg', null=True, upload_to='school_owner_pics'),
        ),
    ]
