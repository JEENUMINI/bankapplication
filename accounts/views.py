from django.shortcuts import render,redirect
from accounts.forms import accountCreateForm,LoginForm,BalanceChkform,TransferAmount
from accounts.models import accountCreateModel
from accounts.models import TransferDetails

# Create your views here.

def transfer(request):
    form=TransferAmount()
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form=TransferAmount(request.POST)
        if(form.is_valid()):
            mpin=form.cleaned_data.get("mpin")
            amount=form.cleaned_data.get("amount")
            try:
                object=accountCreateModel.objects.get(mpin=mpin)
                balance=object.balance-amount
                object.balance=balance
                object.save()
            except Exception:
                context["form"]=form
                return render(request,"accounts/transferamount.html",context)
            form.save()
            return redirect("balance")
        else:
            context["form"]=form
            return render(request,"accounts/transferamount.html",context)
    return render(request,"accounts/transferamount.html",context)

def createAccount(request):
    template_name="accounts/accountcreate.html"
    form=accountCreateForm()
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form=accountCreateForm(request.POST)
        if(form.is_valid()):
            personname=form.cleaned_data.get("personname")
            accountnumber=form.cleaned_data.get("accountnumber")
            accounttype=form.cleaned_data.get("accounttype")
            balance=form.cleaned_data.get("balance")
            phonenumber=form.cleaned_data.get("phonenumber")
            mpin=form.cleaned_data.get("mpin")
            account=accountCreateModel(personname=personname,accountnumber=accountnumber,accounttype=accounttype,balance=balance,phonenumber=phonenumber,mpin=mpin)
            account.save()
            return redirect("accountlist")
    return render(request,template_name,context)

def createModel(request):
    account=accountCreateModel.objects.all()
    context={}
    context["account"]=account
    return render(request,"accounts/accountlist.html",context)

def loginView(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form=LoginForm(request.POST)
        if(form.is_valid()):
            phonenumber=form.cleaned_data.get("phonenumber")
            mpin=form.cleaned_data.get("mpin")
            try:
                object=accountCreateModel.objects.get(phonenumber=phonenumber)
                if ((object.phonenumber == phonenumber) & (object.mpin == mpin)):
                    print("user is exist")
                    return render(request,"accounts/accounthome.html")
            except Exception as e:
                print("invalid credentials")
                context["form"] = form
                return render(request, "accounts/login.html", context)
    return render(request,"accounts/login.html",context)

def balanceEnq(request):
    form=BalanceChkform()
    context={}
    context["form"]=form
    if(request.method=='POST'):
        form=BalanceChkform(request.POST)
        if(form.is_valid()):
            mpin=form.cleaned_data.get("mpin")
            try:
                object=accountCreateModel.objects.get(mpin=mpin)
                context["balance"]=object.balance
                return render(request,"accounts/checkbalance.html",context)
            except Exception as e:
                context["form"]=form
                return render(request,"accounts/checkbalance.html",context)
    return render(request,"accounts/checkbalance.html",context)

def accountActivity(request):
    form=BalanceChkform()
    context={}
    context["form"]=form
    if request.method=='POST':
        form=BalanceChkform(request.POST)
        if(form.is_valid()):
            mpin=form.cleaned_data.get("mpin")
            person_details=accountCreateModel.objects.get(mpin=mpin)
            transactions=TransferDetails.objects.filter(mpin=mpin)
            context["transactions"]=transactions
            context["person_details"]=person_details
            return render(request,"accounts/accounthistory.html",context)
    return render(request,"accounts/accounthistory.html",context)


