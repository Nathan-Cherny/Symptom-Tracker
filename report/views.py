from django.contrib.auth import get_user_model
from django.shortcuts import render

from .forms import ReportForm
from .models import Report

User = get_user_model()


def index(request):
    if request.method == 'POST':
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']

        match data['diagnosed']:
            case "I haven't been diagnosed with anything recently":
                data['diagnosed'] = 'nothing'
            case "COVID 19":
                data['diagnosed'] = 'covid'
            case "Common Cold":
                data['diagnosed'] = 'common cold'
            case "Stomach Bug":
                data['diagnosed'] = 'stomach bug'

        report = {
            'user': User.objects.get(email=request.session['user']['userinfo']['email']),
            'data': data
        }

        Report.objects.create(**report)

    form = ReportForm()
    return render(request, 'report.html', context={
        'form': form,
        "session": request.session.get("user"),
    })
