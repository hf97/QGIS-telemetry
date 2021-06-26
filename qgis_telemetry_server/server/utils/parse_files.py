from django.utils import timezone
from ..models import Telemetry, Action, Location, Plugin, Os, Language, Qgis_version, Ui_theme, Locale, Interface, Server, Added_layer
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
        interface.language = language
        interface.qgis_version = version
        interface.ui_theme = ui_theme
        interface.locale = locale
        interface.os = os
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
    # TODO meter o action em try except
    try:
        action_entry = Action()
        action_entry.name = action['type']
        action_entry.date_time = datetime.strptime(action['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z')
        action_entry.telemetry = telemetry
        action_entry.interface = interface
        action_entry.plugin = plugin
        action_entry.save()
        print("action - start_action :", action_entry)
    except:
        print("No action - start_action")
# -----------------------------------------------


# parse close action ----------------------------
def close_action(action, telemetry):
    action_entry = Action()
    action_entry.name = action['type']
    action_entry.date_time = datetime.strptime(action['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z')
    action_entry.telemetry = telemetry
    action_entry.save()
    print("action:", action_entry)
# -----------------------------------------------


# parse added layer -----------------------------
def added_layer_action(action, telemetry):
    try:
        try:
            added_layer = Added_layer.objects.filter(name=action['name']).filter(extension=action['extension'])[0]
        except:
            print("2")
            added_layer = Added_layer()
            added_layer.name = action['name']
            added_layer.extension = action['extension']
            added_layer.save()
            print("added_layer: ", added_layer)
    except:
        print("No added_layer")
    try:
        action_added_layer = Action()
        action_added_layer.name = action['type']
        action_added_layer.date_time = datetime.strptime(action['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z')
        action_added_layer.telemetry = telemetry
        action_added_layer.added_layer = added_layer
        action_added_layer.save()
        print("action - added_layer: ", action_added_layer)
    except:
        print("No action - added_layer")
# -----------------------------------------------


# parse added layer -----------------------------
def server_action(action, telemetry):
    try:
        try:
            server = Server.objects.filter(protocol=action['protocol'])[0]
            print("server1: ", server)
        except:
            server = Server()
            server.protocol = action['protocol']
            server.save()
            print("server: ", server)
    except:
        print("No server")
    try:
        action_server = Action()
        action_server.name = action['type']
        action_server.date_time = datetime.strptime(action['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z')
        action_server.telemetry = telemetry
        action_server.server = server
        action_server.save()
        print("action - server: ", action_server)
    except:
        print("No action - server")
# -----------------------------------------------


# main function ---------------------------------
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
        telemetry.location = location
        telemetry.save()
        print("telemetry:",telemetry)
        # ------------------------
        for action in info[session]:
            if action['type'] == "start":
                start_action(action, telemetry)
            elif action['type'] == "close":
                close_action(action, telemetry)
            elif action['type'] == "addedLayer":
                added_layer_action(action, telemetry)
            elif action['type'] == "server":
                server_action(action,telemetry)