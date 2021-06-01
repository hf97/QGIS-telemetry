from django.utils import timezone
from ..models import Telemetry, Action, Location, Plugin, Provider, Os, Language, Qgis_version, Ui_theme, Locale, Interface, Server
from datetime import datetime


# parse start action ----------------------------
def start_action(action, telemetry):
    # os --------------------~
    try:
        try:
            os = Os.objects.filter(name=action['interface']['OS'])[0]
        except:
            os = Os()
            os.name = action['interface']['OS']
            os.save()
            print("os:",os)
    except:
        print("No os")
    # -----------------------
    # language --------------
    try:
        try:
            language = Language.objects.filter(name=action['interface']['language'])[0]
        except:
            language = Language()
            language.name = action['interface']['language']
            language.save()
            print("language:",language)
    except:
        print("No language")
    # -----------------------
    # locale ----------------
    try:
        try:
            locale = Locale.objects.filter(name=action['interface']['locale'])[0]
        except:
            locale = Locale()
            locale.name = action['interface']['locale']
            locale.save()
            print("locale:",locale)
    except:
        print("No locale")
    # -----------------------
    # ui_theme --------------
    try:
        try:
            ui_theme = Ui_theme.objects.filter(name=action['interface']['uiTheme'])[0]
        except:
            ui_theme = Ui_theme()
            ui_theme.name = action['interface']['uiTheme']
            ui_theme.save()
            print("ui_theme:",ui_theme)
    except:
        print("No ui_theme")
    # -----------------------
    # version ---------------
    try:
        try:
            version = Qgis_version.objects.filter(name=action['interface']['version'])[0]
        except:
            version = Qgis_version()
            version.name = action['interface']['version']
            version.save()
            print("version:",version)
    except:
        print("No version")
    # -----------------------
    # interface -------------
    try:
        interface = Interface()
        interface.language_id = language
        interface.qgis_version_id = version
        interface.ui_theme_id = ui_theme
        interface.locale_id = locale
        interface.os_id = os
        interface.save()
        print("interface:",interface)
    except:
        interface = Interface()
        # interface.save()
        print("interfacee:",interface)
    # -----------------------
    # plugins ---------------
    for action_plugin in action['plugins'].keys():
        try:
            plugin = Plugin.objects.filter(name=action_plugin).filter(version=action['plugins'][action_plugin]['version'])[0]
        except:
            plugin = Plugin()
            plugin.name = action_plugin
            plugin.version = action['plugins'][action_plugin]['version']
            plugin.save()
            print("plugin:",plugin)
    action_entry = Action()
    action_entry.name = action['type']
    action_entry.date_time = datetime.strptime(action['datetime'], '%Y-%m-%dT%H:%M:%S.%f')
    action_entry.telemetry_id = telemetry
    action_entry.interface_id = interface
    action_entry.plugin_id = plugin
    action_entry.save()
    print("action:", action_entry)
# -----------------------------------------------


# parse close action ----------------------------
def close_action(action, telemetry):
    action_entry = Action()
    action_entry.name = action['type']
    action_entry.date_time = datetime.strptime(action['datetime'], '%Y-%m-%dT%H:%M:%S.%f')
    action_entry.telemetry_id = telemetry
    action_entry.save()
    print("action:", action_entry)
# -----------------------------------------------


def parse_files(ip_location, info):
    print(ip_location)
    print(info)
    for session in info.keys():
        # location ---------------
        try:
            location = Location.objects.filter(name=ip_location)[0]
        except:
            location = Location()
            location.name = ip_location
            location.save()
            print("location:",location)
        # ------------------------
        # telemetry --------------
        telemetry = Telemetry()
        telemetry.date_time = timezone.now()
        telemetry.location_id = location
        telemetry.save()
        print("telemetry:",telemetry)
        # ------------------------
        # print("session:",session)
        for action in info[session]:
            # print("action:",action)
            if action['type'] == "start":
                start_action(action, telemetry)
            elif action['type'] == "close":
                close_action(action, telemetry)