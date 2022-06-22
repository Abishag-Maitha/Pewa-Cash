from django.contrib import admin
from .models import Account, Loan,Payment

# Register your models here.
admin.site.register(Account)
admin.site.register(Loan)
admin.site.register(Payment)
