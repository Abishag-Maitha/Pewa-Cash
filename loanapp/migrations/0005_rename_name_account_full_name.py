# Generated by Django 4.0.5 on 2022-06-22 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loanapp', '0004_alter_loan_loan_term'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='name',
            new_name='Full_Name',
        ),
    ]
