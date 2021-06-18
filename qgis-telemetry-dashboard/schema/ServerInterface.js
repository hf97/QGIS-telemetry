cube(`ServerInterface`, {
  sql: `SELECT * FROM public.server_interface`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    ServerQgisVersion: {
      sql: `${CUBE}.qgis_version_id = ${ServerQgisVersion}.qgis_version_id`,
      relationship: `belongsTo`
    },
    ServerUiTheme: {
      sql: `${CUBE}.ui_theme_id = ${ServerUiTheme}.ui_theme_id`,
      relationship: `belongsTo`
    },
    ServerLanguage: {
      sql: `${CUBE}.language_id = ${ServerLanguage}.language_id`,
      relationship: `belongsTo`
    },
    // ServerQgisVersion: {
    //   sql: `${CUBE}.qgis_version_id = ${ServerQgisVersion}.qgis_version_id`,
    //   relationship: `belongsTo`
    // },
    ServerLocale: {
      sql: `${CUBE}.locale_id = ${ServerLocale}.locale_id`,
      relationship: `belongsTo`
    },
    ServerOs: {
      sql: `${CUBE}.os_id = ${ServerOs}.os_id`,
      relationship: `belongsTo`
    },
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: []
    },
    uiCount: {
      sql:`${countUi}`,
      type: `count`,
      title:`Ui themes`,

    },
    languageCount: {
      sql:`${countLanguage}`,
      type: `count`,
      // title:`Ui themes`,

    },
    qgisVersionCount: {
      sql:`${countQgisVersion}`,
      type: `count`,
      // title:`Ui themes`,

    },
    localeCount: {
      sql:`${countLocale}`,
      type: `count`,
      // title:`Ui themes`,

    },
    osCount: {
      sql:`${countOs}`,
      type: `count`,
      // title:`Ui themes`,

    },
  },
  
  dimensions: {
    interface_id: {
      sql: `interface_id`,
      type: `number`,
      primaryKey: true
    },
    countUi: {
      sql: `${ServerUiTheme.count}`,
      type: `number`,
      subQuery: true
    },
    countLanguage: {
      sql: `${ServerLanguage.count}`,
      type: `number`,
      subQuery: true
    },
    countQgisVersion: {
      sql: `${ServerQgisVersion.count}`,
      type: `number`,
      subQuery: true
    },
    countLocale: {
      sql: `${ServerLocale.count}`,
      type: `number`,
      subQuery: true
    },
    countOs: {
      sql: `${ServerOs.count}`,
      type: `number`,
      subQuery: true
    },
  },
  
  dataSource: `default`
});
