import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

# Create your models here.
class Account(models.Model):  
    Full_Name=models.CharField(max_length=100)
    photo = CloudinaryField('image')
    email = models.EmailField(max_length=30, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='account')
    MobileNo=models.PositiveIntegerField()
    ID_card=CloudinaryField('image')
    datecreated= models.DateField(auto_now_add=True )

    def __str__(self):
        return f'{self.user.username} Account'

    @receiver(post_save, sender=User)
    def create_user_account(sender, instance, created, **kwargs):
        if created:
            Account.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_account(sender, instance, **kwargs):
        instance.account.save()
 
    def save_account(self):
        self.user

    def delete_account(self):
        self.delete()


LOAN_LIMITS = [
(1,'5000'),
(2,'10000'),
(3,'15000'),
(4,'20000'),
(5,'25000'),
(6,'30000'),

]
LOAN_TERM = [
(1,'1'),
(2,'3'),
(3,'4'),
(4,'6'),
]

class Loan(models.Model):
    Loan_Amount=models.PositiveIntegerField(choices = LOAN_LIMITS,default= 0)
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='loan')
    Loan_Term=models.IntegerField(choices=LOAN_TERM, default=0)
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
