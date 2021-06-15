cube(`ServerAddedLayer`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_added_layer`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [name, dateTime]
    }
  },
  
  dimensions: {
    added_layer_id: {
      sql: `added_layer_id`,
      type: `number`,
      primaryKey: true
    },
    
    extension: {
      sql: `extension`,
      type: `string`
    },
    
    name: {
      sql: `name`,
      type: `string`
    },
    
    dateTime: {
      sql: `date_time`,
      type: `time`
    }
  },
  
  dataSource: `default`
});
