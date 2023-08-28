from django.db.models import Count, Window, F, functions
from django.http import JsonResponse, HttpResponse
from alarms.models import Producer


def get_producer_alarms_report(request):
    page = int(request.GET.get("page", 1))
    size = int(request.GET.get("size", 10))
    print("page=", page)
    start = (page - 1) * size
    end = page * size
    print(f"start={start}, end={end}")

    producer_ids = Producer.objects.order_by("display_name").values("id")[start:end]

    producer_alarms = (
        Producer.objects.values(
            "id", "display_name", "alarm__alarm_code__id", "alarm__alarm_code__name"
        )
        .filter(id__in=producer_ids)
        .annotate(
            alarm_count=Count("alarm__alarm_code__id"),
        )
        .annotate(
            alarm_rank=Window(
                expression=functions.RowNumber(),
                partition_by=F("id"),
                order_by="-alarm_count",
            ),
        )
        .filter(alarm_rank__lte=2)
        .order_by("display_name", "alarm_rank")
    )

    producers_with_top_two_alarms = []
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
            if current_alarm:
                producers_with_top_two_alarms[-1]["alarms"].append(current_alarm)
        else:
            producers_with_top_two_alarms.append(
                {
                    "id": pa["id"],
                    "name": pa["display_name"],
                    "alarms": [current_alarm] if current_alarm else [],
                }
            )
            prev_producer_id = pa["id"]
    return producers_with_top_two_alarms


def report(request):
    return JsonResponse(get_producer_alarms_report(request), safe=False)


def report_debug(request):
    return HttpResponse(
        "<html><body><h1>Pouet</h1><pre>"
        + str(get_producer_alarms_report(request))
        + "</pre></body></html>"
    )
