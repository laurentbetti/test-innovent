from django.db import models

# TODO: put common fields in a parent class?


class AlarmCode(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField()
    criticality = models.CharField(max_length=10)
    enabled = models.BooleanField()
    producer_type_id = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField()
    created_by_id = models.IntegerField()
    updated_at = models.DateTimeField()
    updated_by_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "alarmcodes"

    def __str__(self):
        return str(self.name)


class Producer(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.TextField()
    power_station_id = models.IntegerField()
    producer_type_id = models.IntegerField()
    display_name = models.CharField(max_length=100)
    power_curve_min_id = models.IntegerField()
    power_curve_moy_id = models.IntegerField()
    ordinal = models.IntegerField()
    commissioned_at = models.DateTimeField()
    created_at = models.DateTimeField()
    created_by_id = models.IntegerField()
    updated_at = models.DateTimeField()
    updated_by_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "producers"

    def __str__(self):
        return str(self.display_name)


class Alarm(models.Model):
    id = models.IntegerField(primary_key=True)
    time = models.DateTimeField()
    alarm_code = models.ForeignKey(
        AlarmCode, null=True, on_delete=models.SET_NULL, db_column="alarm_code_id"
    )
    producer = models.ForeignKey(
        Producer, null=True, on_delete=models.SET_NULL, db_column="producer_id"
    )
    created_at = models.DateTimeField()
    created_by_id = models.IntegerField()
    updated_at = models.DateTimeField()
    updated_by_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "alarms"

    def __str__(self):
        return f"{self.alarm_code} - {self.time}"
