# Generated by Django 4.1.3 on 2022-12-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_chapter_options_alter_courserating_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='techs',
            field=models.TextField(null=True),
        ),
    ]
