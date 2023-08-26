from django.db.models import Count
from django.http import JsonResponse
from alarms.models import Producer


def report(request):
    producer_alarms = (
        Producer.objects.values(
            "id", "display_name", "alarm__alarm_code__id", "alarm__alarm_code__name"
        )
        .annotate(alarm_count=Count("alarm__alarm_code__id"))
        .order_by("display_name", "-alarm_count")
    )

    producers_with_top_two_alarms = []
    nb_alarms = 0
    prev_producer_id = None
    for pa in producer_alarms:
        current_alarm = (
            {
                "id": pa["alarm__alarm_code__id"],
                "name": pa["alarm__alarm_code__name"],
                "count": pa["alarm_count"],
            }
            if pa["alarm__alarm_code__id"]
            else None
        )
        if pa["id"] == prev_producer_id:
            if nb_alarms < 2 and current_alarm:
                producers_with_top_two_alarms[-1]["alarms"].append(current_alarm)
                nb_alarms += 1
        else:
            producers_with_top_two_alarms.append(
                {
                    "id": pa["id"],
                    "name": pa["display_name"],
                    "alarms": [current_alarm] if current_alarm else [],
                }
            )
            prev_producer_id = pa["id"]
            nb_alarms = 1

    return JsonResponse(producers_with_top_two_alarms, safe=False)
