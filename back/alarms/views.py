from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from alarms.models import Alarm


def report(request):
    data = list(
        Alarm.objects.values("producer_id", "alarm_code")
        .annotate(alarm_count=Count("time"))
        .order_by("producer_id", "-alarm_count")
    )

    # TODO: see if there is a better alternative that safe=False
    return JsonResponse(data, safe=False)
