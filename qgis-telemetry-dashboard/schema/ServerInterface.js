cube(`ServerInterface`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_interface`,
  
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
    }
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: []
    },
    uiCount: {
      sql:`${count2}`,
      type: `sum`
    }
  },
  
  dimensions: {
    interface_id: {
      sql: `interface_id`,
      type: `number`,
      primaryKey: true
    },
    count2: {
      sql: `${ServerUiTheme.count}`,
      type: `number`,
      subQuery: true
    }
  },
  
  dataSource: `default`
});
