from django.contrib import admin
from .models import Telemetry, Action, Location, Plugin, Provider, Os, Language, Qgis_version, Ui_theme, Locale, Interface, Server, Added_layer


# Register your models here.
admin.site.register(Telemetry)
admin.site.register(Action)
admin.site.register(Location)
admin.site.register(Plugin)
admin.site.register(Provider)
admin.site.register(Os)
admin.site.register(Language)
admin.site.register(Qgis_version)
admin.site.register(Ui_theme)
admin.site.register(Locale)
admin.site.register(Interface)
admin.site.register(Server)
admin.site.register(Added_layer)