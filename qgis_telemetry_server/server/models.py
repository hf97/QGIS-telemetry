from django.db import models
from django.utils import timezone

# Create your models here.
# TODO not null onde for preciso
# TODO datetime tem de ser o que vem no ficheiro
class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    def __str__(self):
        return f'id:{self.location_id} name:{self.name}'

    
class Telemetry(models.Model):
    telemetry_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(default=timezone.now)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f'id:{self.telemetry_id} date_time:{self.date_time} location:{self.location_id.name}'


class Plugin(models.Model):
    plugin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    version = models.CharField(max_length=45)
    def __str__(self):
        return f'id:{self.plugin_id} name:{self.name} version:{self.version}'

class Provider(models.Model):
    provider_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'id:{self.provider_id} name:{self.name}'


class Os(models.Model):
    os_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'id:{self.os_id} name:{self.name}'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    def __str__(self):
        return f'id:{self.language_id} name:{self.name}'


class Qgis_version(models.Model):
    qgis_version_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    def __str__(self):
        return f'id:{self.qgis_version_id} name:{self.name}'


class Ui_theme(models.Model):
    ui_theme_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    def __str__(self):
        return f'id:{self.ui_theme_id} name.{self.name}'


class Locale(models.Model):
    locale_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    def __str__(self):
        return f'id:{self.locale_id} name:{self.name}'


class Interface(models.Model):
    interface_id = models.AutoField(primary_key=True)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    qgis_version_id = models.ForeignKey(Qgis_version, on_delete=models.CASCADE)
    ui_theme_id = models.ForeignKey(Ui_theme, on_delete=models.CASCADE)
    locale_id = models.ForeignKey(Locale, on_delete=models.CASCADE)
    os_id = models.ForeignKey(Os, on_delete=models.CASCADE)
    def __str__(self):
        return f'id:{self.interface_id} language:{self.language_id.name} qgis_version:{self.qgis_version_id.name} ui_theme:{self.ui_theme_id.name} location:{self.locale_id.name} os:{self.os_id.name}'


class Server(models.Model):
    server_id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(default=timezone.now)
    protocol = models.CharField(max_length=45)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f'id:{self.server_id} date_time:{self.date_time.name} protocol:{self.protocol} location:{self.location_id.name}'


class Action(models.Model):
    action_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    date_time = models.DateTimeField(default=timezone.now)
    telemetry_id = models.ForeignKey(Telemetry, on_delete=models.CASCADE)
    provider_id = models.ForeignKey(Provider, blank=True, null=True, on_delete=models.CASCADE)
    interface_id = models.ForeignKey(Interface, blank=True, null=True, on_delete=models.CASCADE)
    plugin_id = models.ForeignKey(Plugin, blank=True, null=True, on_delete=models.CASCADE)
    server_id = models.ForeignKey(Server, blank=True, null=True, on_delete=models.CASCADE)
    # def __str__(self):
    #     return f'id:{self.action_id} name:{self.name} telemetry:{self.telemetry_id.telemetry_id} provider:{self.provider_id.name} interface:{self.interface_id.interface_id} plugin:{self.plugin_id.name} server:{self.server_id.server_id}'