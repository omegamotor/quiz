# Generated by Django 2.2.7 on 2020-01-27 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0007_auto_20200127_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='quiz',
        ),
    ]
