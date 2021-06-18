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
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f'id:{self.telemetry_id} date_time:{self.date_time} location:{self.location.name}'


class Plugin(models.Model):
    plugin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    version = models.CharField(max_length=45)
    def __str__(self):
        return f'id:{self.plugin_id} name:{self.name} version:{self.version}'

# class Provider(models.Model):
#     provider_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     def __str__(self):
#         return f'id:{self.provider_id} name:{self.name}'


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


class Added_layer(models.Model):
    added_layer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    extension = models.CharField(max_length=10)
    def __str__(self):
        return f'id:{self.added_layer_id} name:{self.name} extension:{self.extension}'


class Interface(models.Model):
    interface_id = models.AutoField(primary_key=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    qgis_version = models.ForeignKey(Qgis_version, on_delete=models.CASCADE)
    ui_theme = models.ForeignKey(Ui_theme, on_delete=models.CASCADE)
    locale = models.ForeignKey(Locale, on_delete=models.CASCADE)
    os = models.ForeignKey(Os, on_delete=models.CASCADE)
    def __str__(self):
        return f'id:{self.interface_id} language:{self.language.name} qgis_version:{self.qgis_version.name} ui_theme:{self.ui_theme.name} location:{self.locale.name} os:{self.os.name}'


class Server(models.Model):
    server_id = models.AutoField(primary_key=True)
    protocol = models.CharField(max_length=45)
    def __str__(self):
        return f'id:{self.server_id} protocol:{self.protocol}'


class Action(models.Model):
    action_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    date_time = models.DateTimeField(default=timezone.now)
    telemetry = models.ForeignKey(Telemetry, on_delete=models.CASCADE)
    interface = models.ForeignKey(Interface, blank=True, null=True, on_delete=models.CASCADE)
    plugin = models.ForeignKey(Plugin, blank=True, null=True, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, blank=True, null=True, on_delete=models.CASCADE)
    added_layer = models.ForeignKey(Added_layer, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'id:{self.action_id} name:{self.name} date_time:{self.date_time}'