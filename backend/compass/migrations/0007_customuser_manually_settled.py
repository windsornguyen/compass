# Generated by Django 4.2.7 on 2023-12-11 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0006_remove_course_pu_flag_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='manually_settled',
            field=models.JSONField(db_index=True, null=True),
        ),
    ]
