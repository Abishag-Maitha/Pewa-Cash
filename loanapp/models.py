import uuid
from django.db import models
from decimal import ROUND_HALF_UP, Decimal
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.forms import DecimalField
from django.utils import timezone
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Account(models.Model):
    name=models.TextField(max_length=100)
    photo = CloudinaryField('image')
    email = models.EmailField(max_length=30, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='account')
    MobileNo=models.PositiveIntegerField()
    ID_card=CloudinaryField('image')
    datecreated= models.DateField(auto_now_add=True )

    def __str__(self):
        return self.user.username
 
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

class Loan(models.Model):
    Loan_Amount=models.DecimalField(max_digits=20, decimal_places=2)
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='loan')
    Loan_Term=models.IntegerField()
    date_borrowed=models.DateField(auto_now_add=True)
    rate = models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self):
            return self.user.username
    
    def save_profile(self):
            self.user

class Payment(models.Model):
   user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='payment')
   loan=models.OneToOneField(Loan, on_delete=models.CASCADE, related_name='payment')
   Amount=models.DecimalField(max_digits=20, decimal_places=2)
