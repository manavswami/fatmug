# Generated by Django 4.2.7 on 2023-12-02 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('on_time_delivery_rate', models.FloatField(blank=True, null=True)),
                ('quality_rating_avg', models.FloatField(blank=True, null=True)),
                ('average_response_time', models.FloatField(blank=True, null=True)),
                ('fulfillment_rate', models.FloatField(blank=True, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vendor_code', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderDetails',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('po_number', models.CharField(max_length=100)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateField()),
                ('items', models.JSONField()),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(choices=[('pending', 'pending'), ('completed', 'completed'), ('canceled', 'canceled')], max_length=100)),
                ('actual_delivery', models.DateField()),
                ('quality_rating', models.FloatField(blank=True, null=True)),
                ('issue_date', models.DateTimeField()),
                ('acknowledgment_date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='VMS.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_time_delivery_rate', models.FloatField(blank=True, null=True)),
                ('quality_rating_avg', models.FloatField(blank=True, null=True)),
                ('average_response_time', models.FloatField(blank=True, null=True)),
                ('fulfillment_rate', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VMS.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
