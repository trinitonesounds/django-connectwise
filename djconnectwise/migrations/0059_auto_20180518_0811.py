# Generated by Django 2.0.5 on 2018-05-18 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0058_auto_20180516_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='callbackentry',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='djconnectwise.Member'),
        ),
    ]