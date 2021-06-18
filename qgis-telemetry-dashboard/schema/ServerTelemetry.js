cube(`ServerTelemetry`, {
  sql: `SELECT * FROM public.server_telemetry`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    ServerAction: {
      relationship: `hasMany`,
      sql: `${ServerTelemetry}.telemetry_id = ${ServerAction}.telemetry_id`,
    },
    ServerLocation: {
      relationship: `hasMany`,
      sql: `${ServerTelemetry}.location_id = ${ServerLocation}.location_id`,
    },
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [dateTime]
    },
    totalCount: {
      sql:`${countUi}`,
      type:`count`,
      title:`Ui themes`,
      description:`Ui themes`,
    },
    totalCountActions: {
      sql:`${countActions}`,
      type:`count`,
      title:`Most used Actions`,
      description:`Most used Actions`,
    },
    totalCountPlugin: {
      sql:`${countPlugin}`,
      type:`count`,
      title:`Plugins`,
      description:`Plugins`,
    },
    totalCountProvider: {
      sql:`${countProvider}`,
      type:`count`,
      title:`Providers`,
      description:`Providers`,
    },
    totalCountServer: {
      sql:`${countServer}`,
      type:`count`,
      title:`Servers`,
      description:`Servers`,
    },
    totalCountLanguage: {
      sql:`${countLanguage}`,
      type:`count`,
      title:`Languages`,
      description:`Languages`,
    },
    totalCountQgisVersion: {
      sql:`${countQgisVersion}`,
      type:`count`,
      title:`Qgis Versions`,
      description:`Qgis Versions`,
    },
    totalCountLocale: {
      sql:`${countLocale}`,
      type:`count`,
      title:`Locale`,
      description:`Locale`,
    },
    totalCountOs: {
      sql:`${countOs}`,
      type:`count`,
      title:`Operative Systems`,
      description:`Operative Systems`,
    },
    totalCountlayers: {
      sql:`${countLayers}`,
      type:`count`,
      title:`Layers`,
      description:`Layers`,
    },
    totalLocation:{
      sql:`${countLocation}`,
      type:`count`,
      title:`Locations`,
      description:`Locations`,
    }
  },
  
  dimensions: {
    countLocation: {
      sql: `${ServerLocation.count}`,
      type: `number`,
      subQuery: true,

    },
    countActions: {
      sql: `${ServerAction.count}`,
      type: `number`,
      subQuery: true,

    },
    countUi: {
      sql: `${ServerAction.actionUICount}`,
      type: `number`,
      subQuery: true,

    },
    countProvider: {
      sql: `${ServerAction.actionProviderCount}`,
      type: `number`,
      subQuery: true,

    },
    countServer: {
      sql: `${ServerAction.actionServerCount}`,
      type: `number`,
      subQuery: true,

    },
    countPlugin: {
      sql: `${ServerAction.actionPluginCount}`,
      type: `number`,
      subQuery: true,

    },
    countLanguage: {
      sql: `${ServerAction.actionLanguageCount}`,
      type: `number`,
      subQuery: true,

    },
    countQgisVersion: {
      sql: `${ServerAction.actionQgisVersionCount}`,
      type: `number`,
      subQuery: true,

    },
    countLocale: {
      sql: `${ServerAction.actionLocaleCount}`,
      type: `number`,
      subQuery: true,

    },
    countOs: {
      sql: `${ServerAction.actionOsCount}`,
      type: `number`,
      subQuery: true,

    },
    countLayers: {
      sql: `${ServerAction.actionLayersCount}`,
      type: `number`,
      subQuery: true,

    },
    telemetry_id: {
      sql: `telemetry_id`,
      type: `number`,
      primaryKey: true
    },
    dateTime: {
      sql: `date_time`,
      type: `time`
    }
  },
  
  dataSource: `default`
});
