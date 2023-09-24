from django.contrib.auth import get_user_model
from django.db.models import F
from django.shortcuts import render

from places.models import Place
from .forms import ReportForm
from .models import Report

User = get_user_model()

stomachBugMultiplier = [0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 0, 0]
covidMultiplier = [2, 1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 1]
coldMultiplier = [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1]


def index(request):
    if request.method == 'POST':
        data = request.POST.dict()

        match data['diagnosed']:
            case "I haven't been diagnosed with anything recently":
                data['diagnosed'] = 'nothing'
            case "COVID 19":
                data['diagnosed'] = 'covid'
            case "Common Cold":
                data['diagnosed'] = 'common cold'
            case "Stomach Bug":
                data['diagnosed'] = 'stomach bug'

        report_data = {
            'user': User.objects.get(email=request.session['user']['userinfo']['email']),
            'diagnosed_with': data.get('diagnosed'),
            'lives_at': data.get('hall'),
            'smoked': data.get('smoked') == 'on',
            'drank': data.get('drink') == 'on',
            'around_sick': data.get('sick') == 'on',
            'symptoms': {
                'cough': data.get('cough') == 'on',
                'fever': data.get('fever') == 'on',
                'chills': data.get('chills') == 'on',
                'smell': data.get('smell') == 'on',
                'fatigue': data.get('fatigue') == 'on',
                'vomit': data.get('vomit') == 'on',
                'nausea': data.get('nausea') == 'on',
                'stomach': data.get('stomach') == 'on',
                'diarrhea': data.get('diarrhea') == 'on',
                'taste': data.get('taste') == 'on',
                'breathing': data.get('breathing') == 'on',
                'nose': data.get('nose') == 'on',
                'throat': data.get('throat') == 'on'
            }
        }

        stomachBugVal = 0
        covidVal = 0
        coldVal = 0

        report = Report.objects.create(**report_data)
        if report.diagnosed_with != 'nothing':
            Place.objects.filter(name=report.lives_at).update(health_score=F('health_score') + 2)
        else:
            symptoms = list(report_data['symptoms'].values())
            print(symptoms)
            for i in range(len(symptoms) - 3):
                stomachBugVal += stomachBugMultiplier[i] * symptoms[i]
                covidVal += covidMultiplier[i] * symptoms[i]
                coldVal += coldMultiplier[i] * symptoms[i]

            stomachBugVal = stomachBugVal - report.drank
            covidVal = covidVal - report.smoked - report.drank + (2 * report.around_sick)
            coldVal = coldVal - report.smoked - report.drank + (2 * report.around_sick)

            stomachBugVal = float(stomachBugVal / sum(stomachBugMultiplier))
            covidVal = float(covidVal / sum(covidMultiplier))
            coldVal = float(coldVal / sum(coldMultiplier))

            if 0.3 < max(stomachBugVal, coldVal, covidVal) < 0.8:
                Place.objects.filter(name=report.lives_at).update(health_score=F('health_score') + 1)
            else:
                Place.objects.filter(name=report.lives_at).update(health_score=F('health_score') + 2)

    form = ReportForm()
    return render(request, 'report.html', context={
        'form': form,
        "session": request.session.get("user"),
    })
