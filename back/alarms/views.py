from django.db.models import Count
from django.http import JsonResponse
from alarms.models import Producer


def report(request):
    producer_alarms = list(
        Producer.objects.values(
            "id", "display_name", "alarm__alarm_code__id", "alarm__alarm_code__name"
        )
        .annotate(trigger_count=Count("alarm__alarm_code__id"))
        .order_by("id", "-trigger_count")
    )

    producer_top_two_alarms = []
    nb_alarms = 0
    prev_producer_id = None
    for pa in producer_alarms:
        if pa["id"] == prev_producer_id:
            if nb_alarms < 2:
                producer_top_two_alarms.append(pa)
                nb_alarms += 1
        else:
            producer_top_two_alarms.append(pa)
            prev_producer_id = pa["id"]
            nb_alarms = 1

    formatted_producer_alarms = list(
        map(
            lambda pa: (
                {
                    "id": pa["id"],
                    "name": pa["display_name"],
                    "alarmCodeId": pa["alarm__alarm_code__id"],
                    "alarmCodeName": pa["alarm__alarm_code__name"],
                    "alarmCount": pa["trigger_count"],
                }
            ),
            producer_top_two_alarms,
        )
    )
    return JsonResponse(formatted_producer_alarms, safe=False)
