from django.db import models

# TODO: put common fields in a parent class?


class AlarmCode(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50, blank=True, null=True)
    # TODO: remove primary_key = true once we have table ids fields
    code = models.CharField(max_length=20, primary_key=True)
    criticality = models.CharField(max_length=10)
    enabled = models.BooleanField()
    # TO IMPROVE: foreign key
    producer_type_id = models.PositiveSmallIntegerField()

    created_at = models.DateTimeField()
    # TO IMPROVE: foreign key
    created_by_id = models.PositiveSmallIntegerField()
    updated_at = models.DateTimeField()
    # TO IMPROVE: foreign key
    updated_by_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = "api_alarmcode"

    def __str__(self):
        return self.name


class Alarm(models.Model):
    time = models.DateTimeField()
    # alarm_code: models.ForeignKey(AlarmCodes, on_delete=models.SET_NULL)
    alarm_code: models.PositiveSmallIntegerField()
    # TO IMPROVE: foreign key
    producer_id = models.PositiveSmallIntegerField()

    # TODO: remove priamry_key=True once we have proper ids
    created_at = models.DateTimeField(primary_key=True)
    # TO IMPROVE: foreign key
    created_by_id = models.PositiveSmallIntegerField()
    updated_at = models.DateTimeField()
    updated_by_id = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = "api_alarms"

    def __str__(self):
        return f"{self.alarm_code} - {self.time}"
