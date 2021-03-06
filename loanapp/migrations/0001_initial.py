# Generated by Django 4.0.5 on 2022-06-21 20:22

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loan_Amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('Loan_Term', models.IntegerField(max_length=2)),
                ('date_borrowed', models.DateField(auto_now_add=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loan', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_Amt', models.DecimalField(decimal_places=2, max_digits=20)),
                ('loan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to='loanapp.loan')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('MobileNo', models.PositiveIntegerField(max_length=20)),
                ('ID_card', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('datecreated', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
