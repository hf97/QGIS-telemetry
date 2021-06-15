cube(`ServerPlugin`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_plugin`,
  
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
    plugin_id: {
      sql: `plugin_id`,
      type: `number`,
      primaryKey: true
    },
    version: {
      sql: `version`,
      type: `string`
    },
    
    name: {
      sql: `name`,
      type: `string`
    }
  },
  
  dataSource: `default`
});
