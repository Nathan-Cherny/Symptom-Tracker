from datetime import timedelta

from .models import Report


def delete_report():
    for report in Report.objects.filter(created_at__lte=timedelta(seconds=10)):
        print(report)
        report.delete()
