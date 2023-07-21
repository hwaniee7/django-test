from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, resolve_url
from django.db.models import Q
from .models import AccountTest

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))


def accountList(request):
    accountList = AccountTest.objects.all().values()
    #print(accountList)
    context = {
        'accountList': accountList,
    }
    return render(request, 'accountlist.html', context)
