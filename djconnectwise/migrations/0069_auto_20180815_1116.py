# Generated by Django 2.0 on 2018-08-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djconnectwise', '0068_merge_20180814_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeentry',
            name='billable_option',
            field=models.CharField(choices=[('Billable', 'Billable'), ('DoNotBill', 'Do Not Bill'), ('NoCharge', 'No Charge'), ('NoDefault', 'No Default')], max_length=250),
        ),
        migrations.AlterField(
            model_name='timeentry',
            name='charge_to_type',
            field=models.CharField(choices=[('ServiceTicket', 'Service Ticket'), ('ProjectTicket', 'Project Ticket'), ('ChargeCode', 'Charge Code'), ('Activity', 'Activity')], max_length=250),
        ),
    ]
