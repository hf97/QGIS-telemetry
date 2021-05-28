from django.db import models
from django.utils import timezone

# Create your models here.
# TODO not null onde for preciso
# TODO datetime tem de ser o que vem no ficheiro
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    def __str__(self):
        return self.name

    
class Telemetry(models.Model):
    telemetry_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(default=timezone.now)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.date_time} {self.location.name}'


class Plugin(models.Model):
    plugin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    version = models.CharField(max_length=45)
    def __str__(self):
        return f'{self.name} {self.version}'

class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'


class Os(models.Model):
    os_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    def __str__(self):
        return f'{self.name}'


class Qgis_version(models.Model):
    qgis_version_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    def __str__(self):
        return f'{self.name}'


class Ui_theme(models.Model):
    ui_theme_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    def __str__(self):
        return f'{self.name}'


class Locale(models.Model):
    locale_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    def __str__(self):
        return f'{self.name}'


class Interface(models.Model):
    interface_id = models.AutoField(primary_key=True)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    qgis_version_id = models.ForeignKey(Qgis_version, on_delete=models.CASCADE)
    ui_theme_id = models.ForeignKey(Ui_theme, on_delete=models.CASCADE)
    locale_id = models.ForeignKey(Locale, on_delete=models.CASCADE)
    os_id = models.ForeignKey(Os, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.language_id.name} {self.qgis_version_id.name} {self.ui_theme_id.name} {self.location_id.name} {self.os_id.name}'


class Server(models.Model):
    server_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(default=timezone.now)
    protocol = models.CharField(max_length=45)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.date_time.name} {self.protocol} {self.location_id.name}'


class Action(models.Model):
    action_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    telemetry_id = models.ForeignKey(Telemetry, on_delete=models.CASCADE)
    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    interface_id = models.ForeignKey(Interface, on_delete=models.CASCADE)
    plugin_id = models.ForeignKey(Plugin, on_delete=models.CASCADE)
    server_id = models.ForeignKey(Server, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} {self.telemetry_id.name} {self.provider_id.name} {self.interface_id.name} {self.plugin_id.name} {self.server_id.name}'