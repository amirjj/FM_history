# Generated by Django 4.0.5 on 2022-06-11 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fscheck', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='querylog',
            old_name='usernamme',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='fraud',
            name='fraud_description',
            field=models.TextField(),
        ),
    ]
