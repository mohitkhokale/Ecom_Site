# Generated by Django 4.0.2 on 2022-02-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0027_alter_userprofile_user_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_img',
            field=models.FileField(blank=True, default='img/profile-img.jpg', null=True, upload_to='media'),
        ),
    ]
