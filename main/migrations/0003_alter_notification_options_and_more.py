# Generated by Django 4.1.3 on 2022-11-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_notification_alter_course_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name_plural': '5. Notifications'},
        ),
        migrations.RemoveField(
            model_name='notification',
            name='notif_text',
        ),
        migrations.AlterField(
            model_name='notification',
            name='notif_for',
            field=models.CharField(max_length=100, verbose_name='Notification for'),
        ),
    ]
