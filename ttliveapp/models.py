from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_code_generator

# Create your models here.
class StationModel(models.Model):
    name = models.CharField(max_length=120, blank=True)
    digital_address = models.CharField(max_length=200, blank=True)
    master_info = models.FileField(blank=True,)
    contact = models.CharField(max_length=120, blank=True)
    photo = models.ImageField(upload_to='station_photos', blank=True)

    def __str__(self):
        return self.name


class MissingItem(models.Model):
    # user = models.ForeignKey()
    station = models.ForeignKey(StationModel, on_delete=models.DO_NOTHING)
    time = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)
    origin = models.CharField(max_length=120, blank=True)
    drop_point = models.CharField(max_length=120, blank=True)



class Routes(models.Model):
    station = models.ForeignKey(StationModel, on_delete=models.DO_NOTHING)
    shortname = models.CharField(max_length=120, blank=True)
    longname = models.CharField(max_length=120, blank=True)
    route_type = models.CharField(max_length=120, blank=True)

    def __str__(self):
        self.shortname

    class Meta:
        verbose_name = 'Route'
        verbose_name_plural = 'Routes'

class FareRules(models.Model):
    route = models.ForeignKey(Routes, on_delete=models.DO_NOTHING)
    origin = models.CharField(max_length=120, blank=True)
    destination = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.origin

    class Meta:
        verbose_name = 'Fare_rule'
        verbose_name_plural = 'Fare_rules'


class Trip(models.Model):
    route = models.ForeignKey(Routes, on_delete=models.DO_NOTHING)
    headsign = models.CharField(max_length=120)
    station = models.ForeignKey(StationModel, on_delete=models.DO_NOTHING)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.headsign


class Stops(models.Model):
    code = models.SlugField(unique=True, blank=True)
    name = models.CharField(max_length=120, blank=True)
    lat = models.PositiveIntegerField()
    long = models.PositiveIntegerField()
    digital_address = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'stop'
        verbose_name_plural = 'Stops'


def stop_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.code:
        instance.code = unique_code_generator(instance)

pre_save.connect(stop_pre_save_receiver, sender=Stops)




