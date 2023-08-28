from django.urls import path

from . import views

urlpatterns = [
    path("report/", views.report, name="report"),
    path("report-debug/", views.report_debug, name="report_debug"),
]
