from django.db import models


# Create your models here.

class accountCreateModel(models.Model):
    personname=models.CharField(max_length=120)
    accountnumber=models.IntegerField()
    accounttype=models.CharField(max_length=120)
    balance=models.IntegerField(default=3000)
    phonenumber=models.CharField(max_length=12,unique=True)
    mpin=models.CharField(max_length=6,unique=True)

    def __str__(self):
        return self.personname

class TransferDetails(models.Model):
    mpin=models.CharField(max_length=6)
    accountnumber=models.CharField(max_length=15)
    amount=models.IntegerField()

    def __str__(self):
        return self.mpin+self.accountnumber
