# QGIS Enhancement: QGIS Telemetry

**Authors** 
- Hugo Ferreira (@hf97)
- Filipe Barbosa (@flipsboy)
- Nuno Morais (@dancrossss)
- Áureo Benedito (@AureoBenedito)
- Jorge Rocha (@jgrocha)

**Contacts**
- hugoanf97 at gmail dot com
- filipebarbosa96 at hotmail dot com
- a77368 at alunos dot uminho dot pt
- aureojoel3 at gmail dot com
- jgr at geomaster dot pt

# Summary

This proposal is being developed as a project of University of Minho computer science degree under the guidance of teacher Jorge Gustavo Rocha, avid contributer to the qgis community.

Nowadays, most software resort to some form of telemetry to improve user experience.

#### [qgis](https://gitlab.com/jgrocha/qgis-telemetry/-/tree/master/qgis)

Functions to be used in QGIS application to save the telemetry to the json file. The startup.py file should be put in the AppData/Roaming/QGIS/QGIS3 directory.
The rest should be put in the macros section of the QGIS application.

#### [qgis_telemetry_server](https://gitlab.com/jgrocha/qgis-telemetry/-/tree/master/qgis_telemetry_server)

Django server that receives the json telemetry files in /jsonfile directory. It parses the data and sends to a database.

#### [qgis-telemetry-dashboard](https://gitlab.com/jgrocha/qgis-telemetry/-/tree/master/qgis-telemetry-dashboard)

With Cubejs framework, the database is connected to the dashboard and are generated data graphs in a react client.


## Proposed Solution

#### Schema

<img src="https://gitlab.com/jgrocha/qgis-telemetry/-/wikis/uploads/2a62d25db11fd2cac3da49541c910229/esquema.png" width="550">

#### Collected data on QGIS Server application

- Protocols. WMS, WFS, WMTS, etc.
- Location.
- Date.


#### Collected data on QGIS Desktop application

The collected data will be the following:

- At start:
  - Version
  - Operative System
  - Active plugins
  - Start time (to estimate usage time)
  - Generate session ID for each running instance
  - Interface:
    - Language
    - Locale
    - UI Theme
- During operation
  - Providers used
    - for each layer added, the provider type is recorded

#### File types.

The telemetry will be saved in a JSON file.

<img src="https://gitlab.com/jgrocha/qgis-telemetry/-/wikis/uploads/945c69ba8a06435df002f73d1ea749ab/json.png" height="750">  

#### Server side additions

The server will receive the files and populate a database with the corresponding data. The aggregated data from this database can be checked from a dashboard.


#### Dashboard and API.

- Versions in use.
- Most used plugins.
- Most used Operating System.
- Most used providers.
- etc.

#### What we collect ?

- Information from QGIS desktop usage provided by users
- Information from QGIS server usage provided by users

#### Sharing

All this information is aggregated and anonymized soon as it is received on the server side. All data goes to a PostgreSQL database. There is no way to recover or isolate data from a specific user. Collected data can be visualized on a usage dashboard, to be developed. Usage data can also be provided via API.


