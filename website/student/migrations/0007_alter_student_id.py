# Generated by Django 4.0.4 on 2022-05-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.CharField(max_length=8, primary_key=True, serialize=False),
        ),
    ]
