from django.shortcuts import render

from .forms import ReportForm


def index(request):
    form = ReportForm()
    return render(request, 'report.html', context={
        'form': form,
        "session": request.session.get("user"),
    })
