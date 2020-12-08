"""bankapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from accounts.views import createAccount,createModel,loginView,balanceEnq,transfer,accountActivity

urlpatterns = [

    path("createaccount",createAccount,name="createaccount"),
    path("accountlist",createModel,name="accountlist"),
    path("login",loginView,name="login"),
    path("balanceEnq",balanceEnq,name="balance"),
    path("transfer",transfer,name="transfer"),
    path("history",accountActivity,name="history"),
]
