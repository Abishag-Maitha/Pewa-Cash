import uuid
from django.db import models
from decimal import ROUND_HALF_UP, Decimal
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.utils.translation import gettext as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    photo = CloudinaryField('images')
    email = models.EmailField(max_length=30, blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
    datecreated= models.DateField(auto_now_add=True )

    def __str__(self):
        return self.user.username
 
    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

class Base(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField( auto_now_add=True)
    active = models.BooleanField( default=True)

    class Meta:
        abstract = True


class Loan(Base):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    term = models.IntegerField()
    rate = models.DecimalField(max_digits=20, decimal_places=2)
    client = models.ForeignKey(on_delete=models.CASCADE)

    def balance(self, date: timezone.datetime = timezone.now()) -> Decimal:
        payments = self.payment_set.filter(payment=Payment.MADE)
        payments = payments.filter(date__lte=date) if date else payments
        debit = self.installment * self.term
        credit = sum(payments.values_list("amount", flat=True))
        return Decimal(debit - credit)

    @property
    def installment(self) -> Decimal:
        rate = Decimal(f"{self.rate}")
        term = Decimal(self.term)
        r = rate / term
        exact_installment = (r + r / ((1 + r) ** term - 1)) * self.amount
        return exact_installment.quantize(Decimal(".00"), rounding=ROUND_HALF_UP)

    @classmethod
    def interest_rate(cls, client: Base, rate: Decimal) -> Decimal:
        prev_loan = Loan.objects.filter(client=client.id).order_by("-date").first()

        if not prev_loan:
            return rate

        if prev_loan.balance(None) > 0:
            raise ValueError("Pending loan")

        missed_payments = Payment.objects.filter(
            payment=Payment.MISSED, loan__in=Loan.objects.filter(client=client.id)
        ).count()

        if missed_payments > 3:
            raise ValueError("Missed too many payments")
        return rate - Decimal("0.02") if not missed_payments else rate + Decimal("0.04")

    def __str__(self) -> str:
        return f"{self.id}"


class Payment(Base):

    MADE = "made"
    MISSED = "missed"
    PAYMENTS = ((MADE, "made"), (MISSED, "missed"))
    loan = models.ForeignKey(to="api.Loan", verbose_name=_("loan"), on_delete=models.CASCADE)
    payment = models.CharField(max_length=6, choices=PAYMENTS, default=MISSED)
    amount = models.DecimalField(max_digits=20, decimal_places=2)

    def validate(self) -> None:
        if self.amount != self.loan.installment:
            raise ValueError(f"You must pay ${self.loan.installment}")

        last_payment = (
            self.loan.payment_set.filter(date__month=self.date.month).order_by("-date", "-updated")
            .first()
        )

        if last_payment and (
            last_payment.date.month == self.date.month
            and last_payment.date.year == self.date.year
        ):
            if (
                last_payment.payment == self.payment
                or last_payment.payment == self.MADE
            ):
                raise ValueError("Only one payment per month")

    def __str__(self) -> str:
        return str(self.id)


class Client(Base):

    name = models.CharField(max_length=255, verbose_name=_("name"))
    surname = models.CharField(max_length=255, verbose_name=_("surname"))
    email = models.EmailField(max_length=255, verbose_name=_("e-mail"))
    telephone = models.CharField(max_length=20, blank=True, verbose_name=_("telephone"))
    date = models.DateTimeField(
        auto_now_add=True, blank=True, verbose_name=_("date of creation")
    )
    cpf = models.CharField(
        max_length=14, unique=True, verbose_name=_("natural persons register")
    )

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self) -> str:
        return str(self.id)