from django.shortcuts import render


def stocks_list(request):
    return render(request, 'stocks/list.html')
