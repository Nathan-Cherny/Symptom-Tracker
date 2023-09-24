from django.shortcuts import render

from .forms import ReportForm

import json


def index(request):
    print(request.method)
    data = request.POST

    print(data.dict())
    form = ReportForm()
    return render(request, 'report.html', context={
        'form': form,
        "session": request.session.get("user"),
    })
    