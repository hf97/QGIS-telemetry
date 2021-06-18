cube(`ServerAction`, {
  sql: `SELECT * FROM public.server_action`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    ServerInterface: {
      relationship: `hasOne`,
      sql: `${ServerAction}.interface_id = ${ServerInterface}.interface_id`,
    },
    ServerPlugin: {
      relationship: `hasMany`,
      sql: `${ServerAction}.plugin_id = ${ServerPlugin}.plugin_id`,
    },
    ServerProvider: {
      relationship: `hasMany`,
      sql: `${ServerAction}.provider_id = ${ServerProvider}.provider_id`,
    },
    ServerServer: {
      relationship: `hasMany`,
      sql: `${ServerAction}.server_id = ${ServerServer}.server_id`,
    },
    ServerAddedLayer: {
      relationship: `hasMany`,
      sql: `${ServerAction}.added_layer_id = ${ServerAddedLayer}.added_layer_id`,
    },
    
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [name, dateTime]
    },
    actionUICount:{
      sql: `${countUi}`,
      type:`count`,
      title:`Ui themes`,

    },
    actionPluginCount:{
      sql: `${countPlugin}`,
      type:`count`,
      title:`Plugins`,
    },
    actionProviderCount:{
      sql: `${countProvider}`,
      type:`count`,
      title:`Providers`,
    },
    actionServerCount:{
      sql: `${countServer}`,
      type:`count`,
      title:`Servers`,
    },
    actionLanguageCount:{
      sql: `${countLanguage}`,
      type:`count`,
      title:`Languages`,
    },
    actionQgisVersionCount:{
      sql: `${countQgisVersion}`,
      type:`count`,
      title:`Versions`,
    },
    actionLocaleCount:{
      sql: `${countLocale}`,
      type:`count`,
      title:`Locales`,
    },
    actionOsCount:{
      sql: `${countOs}`,
      type:`count`,
      title:`Os`,
    },
    actionLayersCount:{
      sql: `${countLayers}`,
      type:`count`,
      title:`Os`,
    },
  },
  
  dimensions: {
    action_id: {
      sql: `action_id`,
      type: `number`,
      primaryKey: true
    },
    
    name: {
      sql: `name`,
      type: `string`
    },
    
    dateTime: {
      sql: `date_time`,
      type: `time`
    },
    countUi: {
      sql: `${ServerInterface.uiCount}`,
      type: `number`,
      subQuery: true
    },
    countPlugin: {
      sql: `${ServerPlugin.count}`,
      type: `number`,
      subQuery: true
    },
    countProvider: {
      sql: `${ServerProvider.count}`,
      type: `number`,
      subQuery: true
    },
    countServer: {
      sql: `${ServerServer.count}`,
      type: `number`,
      subQuery: true
    },
    countLanguage: {
      sql: `${ServerInterface.languageCount}`,
      type: `number`,
      subQuery: true
    },
    countQgisVersion: {
      sql: `${ServerInterface.qgisVersionCount}`,
      type: `number`,
      subQuery: true
    },
    countLocale: {
      sql: `${ServerInterface.localeCount}`,
      type: `number`,
      subQuery: true
    },
    countOs: {
      sql: `${ServerInterface.osCount}`,
      type: `number`,
      subQuery: true
    },
    countLayers: {
      sql: `${ServerAddedLayer.count}`,
      type: `number`,
      subQuery: true
    },
  },
  
  dataSource: `default`
});
