from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.utils import timezone

from .models import Telemetry, Action, Location, Plugin, Provider, Os, Language, Qgis_version, Ui_theme, Locale, Interface, Server

# IP
from django.contrib.gis.geoip2 import GeoIP2

import json
import datetime


from view_helpers.parse_file import *

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'server/index.html')

@csrf_exempt
def jsonfile(request):
    if request.method == "POST":

        
        try:
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
        except:
            ip = request.META.get('REMOTE_ADDR')
        try:
            geo = GeoIP2()
            ip_location = geo.country.name
        except:
            ip_location = "None"
        print("ip:", ip, "ip_location:", ip_location)

        
        for filename in request.FILES:
            uploaded_file = request.FILES[filename]
            dictjson = json.loads(uploaded_file.read())
            info = {}
            for action in dictjson['actions']:
                if action['sessionId'] in info:
                    info[action['sessionId']].append(action)
                else:
                    info[action['sessionId']] = []
                    info[action['sessionId']].append(dict(action))

            # apenas para ver em ficheiro o que recebe
            # f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/teste.json", "w")
            # json.dump(info, f, indent=4)
            # f.close()


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
                        # os --------------------
                        try:
                            os = Os.objects.filter(name=action['interface']['OS'])[0]
                        except:
                            os = Os()
                            os.name = action['interface']['OS']
                            os.save()
                            print("os:",os)
                        # -----------------------
                        # language --------------
                        try:
                            language = Language.objects.filter(name=action['interface']['language'])[0]
                        except:
                            language = Language()
                            language.name = action['interface']['language']
                            language.save()
                            print("language:",language)
                        # -----------------------
                        # locale ----------------
                        try:
                            locale = Locale.objects.filter(name=action['interface']['locale'])[0]
                        except:
                            locale = Locale()
                            locale.name = action['interface']['locale']
                            locale.save()
                            print("locale:",locale)
                        # -----------------------
                        # ui_theme --------------
                        try:
                            ui_theme = Ui_theme.objects.filter(name=action['interface']['uiTheme'])[0]
                        except:
                            ui_theme = Ui_theme()
                            ui_theme.name = action['interface']['uiTheme']
                            ui_theme.save()
                            print("ui_theme:",ui_theme)
                        # -----------------------
                        # version ---------------
                        try:
                            version = Qgis_version.objects.filter(name=action['interface']['version'])[0]
                        except:
                            version = Qgis_version()
                            version.name = action['interface']['version']
                            version.save()
                            print("version:",version)
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
                        action_entry.date_time = datetime.datetime.strptime(action['datetime'], '%Y-%m-%dT%H:%M:%S.%f')
                        action_entry.telemetry_id = telemetry
                        action_entry.interface_id = interface
                        action_entry.plugin_id = plugin
                        action_entry.save()
                        print("action:", action_entry)

                    # elif action['type'] == "close":
                    #     action = Action()
                    #     action.name = action['type']
                    #     action.date_time = action['datetime']



            print(info)
            f = open("C:/Users/hugof/Desktop/QGIS-telemetry/qgis/teste.json", "w")
            json.dump(info, f, indent=4)
            f.close()
            # default_storage.save('./telemetry/'+uploaded_file.name+".json", uploaded_file)
        return render(request, "server/index.html")
