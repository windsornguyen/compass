# Generated by Django 4.2.7 on 2023-12-11 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compass', '0007_customuser_manually_settled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='manually_settled',
        ),
        migrations.AddField(
            model_name='usercourses',
            name='settled',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compass.requirement'),
        ),
    ]