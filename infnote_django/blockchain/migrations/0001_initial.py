# Generated by Django 2.0.6 on 2018-06-25 10:55

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txid', models.CharField(db_index=True, max_length=64)),
                ('vout', models.IntegerField(default=0)),
                ('value', models.BigIntegerField(default=0)),
                ('spendable', models.BooleanField(default=False)),
                ('frozen', models.BooleanField(default=False)),
                ('owner', models.CharField(max_length=34)),
                ('height', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'bc_coin',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(default=-1)),
            ],
            options={
                'db_table': 'bc_info',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True)),
                ('vin', djongo.models.fields.ListField()),
                ('vout', djongo.models.fields.ListField()),
            ],
            options={
                'db_table': 'bc_tx',
            },
        ),
        migrations.AlterUniqueTogether(
            name='coin',
            unique_together={('txid', 'vout')},
        ),
    ]
