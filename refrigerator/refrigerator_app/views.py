from django.shortcuts import render
from refrigerator_app.models import Stock


def stocks_list(request):
    stocks = Stock.objects.all()
    return render(request, 'stocks/list.html', {"stocks": stocks})
