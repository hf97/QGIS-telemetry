from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
# from django.utils import timezone

# from .models import Telemetry, Action, Location, Plugin, Provider, Os, Language, Qgis_version, Ui_theme, Locale, Interface, Server

# IP
import geoip2.database

import json
# import datetime

from .utils.parse_files import *

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, 'server/index.html')

@csrf_exempt
def jsonfile(request):
    if request.method == "POST":
        reader = geoip2.database.Reader("./GeoLite2-Country_20210615/GeoLite2-Country.mmdb")
        try:
            ip = request.META.get('HTTP_X_FORWARDED_FOR')
        except:
            ip = request.META.get('REMOTE_ADDR')
        try:
            response = reader.country(ip)
            ip_location = response.registered_country.name['en']
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

            parse_files(ip_location, info)

            # default_storage.save('./telemetry/'+uploaded_file.name+".json", uploaded_file)
        return render(request, "server/index.html")
