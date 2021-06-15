cube(`ServerUiTheme`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_ui_theme`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [name]
    }
  },
  
  dimensions: {
    ui_theme_id: {
      sql: `ui_theme_id`,
      type: `number`,
      primaryKey: true
    },
    name: {
      sql: `name`,
      type: `string`
    }
  },
  
  dataSource: `default`
});
