# Generated by Django 2.1.11 on 2019-08-16 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0108_projectphase'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='phase',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='phase_tickets', to='djconnectwise.ProjectPhase'),
        ),
    ]
