from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'mo_bank/index.html')

def register(request):
    return render(request, 'mo_bank/open account.html')