# Generated by Django 4.0.2 on 2022-02-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0024_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=255),
        ),
    ]
