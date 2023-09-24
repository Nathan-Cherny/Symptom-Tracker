from django.contrib.auth import get_user_model
from django.db.models import F
from django.shortcuts import render

from places.models import Place
from .forms import ReportForm
from .models import Report

User = get_user_model()


def index(request):
    if request.method == 'POST':
        data = request.POST.dict()

        print(data)

        match data['diagnosed']:
            case "I haven't been diagnosed with anything recently":
                data['diagnosed_with'] = 'nothing'
            case "COVID 19":
                data['diagnosed_with'] = 'covid'
            case "Common Cold":
                data['diagnosed_with'] = 'common cold'
            case "Stomach Bug":
                data['diagnosed_with'] = 'stomach bug'

        report_data = {
            'user': User.objects.get(email=request.session['user']['userinfo']['email']),
            'diagnosed_with': data.get('diagnosed'),
            'lives_at': data.get('hall'),
            'smoked': data.get('smoked'),
            'drank': data.get('drank'),
            'around_sick': data.get('around_sick')
        }

        print(report_data)

        # report = Report.objects.create(**report_data)
        # if not report.diagnosed_with == 'nothing':
        #     Place.objects.filter(name=report.lives_at).update(health_score=F('health_score') + 2)

    form = ReportForm()
    return render(request, 'report.html', context={
        'form': form,
        "session": request.session.get("user"),
    })
