# Generated by Django 4.0.5 on 2022-06-22 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0003_rename_payment_amt_payment_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='Loan_Term',
            field=models.IntegerField(choices=[(1, '1'), (2, '3'), (3, '4'), (4, '6')], default=0),
        ),
    ]