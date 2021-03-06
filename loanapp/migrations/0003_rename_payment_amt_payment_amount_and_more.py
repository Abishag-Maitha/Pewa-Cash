# Generated by Django 4.0.5 on 2022-06-21 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0002_alter_account_mobileno_alter_loan_loan_term'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_Amt',
            new_name='Amount',
        ),
        migrations.AlterField(
            model_name='loan',
            name='Loan_Amount',
            field=models.PositiveIntegerField(choices=[(1, '5000'), (2, '10000'), (3, '15000'), (4, '20000'), (5, '25000'), (6, '30000')], default=0),
        ),
    ]
