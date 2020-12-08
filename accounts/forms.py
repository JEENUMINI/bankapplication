from django import forms
from django.forms import ModelForm
from accounts.models import TransferDetails,accountCreateModel

class accountCreateForm(forms.Form):
    personname=forms.CharField(max_length=150)
    accountnumber=forms.CharField(max_length=18)
    accounttype=forms.CharField(max_length=50)
    balance=forms.IntegerField()
    phonenumber=forms.CharField(max_length=12)
    mpin=forms.CharField(max_length=6)

class LoginForm(forms.Form):
    phonenumber=forms.CharField(max_length=15)
    mpin=forms.CharField(max_length=6)

class BalanceChkform(forms.Form):
    mpin=forms.CharField(max_length=6)

    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        try:
            object=accountCreateModel.objects.get(mpin=mpin)
        except:
            msg="you are provided invalid mpin"
            self.add_error("mpin",msg)


class TransferAmount(ModelForm):
    class Meta:
        model=TransferDetails
        fields="__all__"
    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        accountnumber=cleaned_data.get("accountnumber")
        amount=cleaned_data.get("amount")
        print(mpin,",",accountnumber,",",amount)
        try:
            object=accountCreateModel.objects.get(mpin=mpin)
            if(object):
                if(object.balance<amount):
                    msg="insufficient balance in your account"
                    self.add_error("amount",msg)
        except:
            msg = "you are provided invalid mpin"
            self.add_error("mpin", msg)


        try:
            object=accountCreateModel.objects.get(accountnumber=accountnumber)

            if(object):
                pass
        except:
            msg="you are provided invalid account number"
            self.add_error("accountnumber",msg)






