cube(`ServerServer`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_server`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [dateTime]
    }
  },
  
  dimensions: {
    server_id: {
      sql: `server_id`,
      type: `number`,
      primaryKey: true
    },
    protocol: {
      sql: `protocol`,
      type: `string`
    },
    
    dateTime: {
      sql: `date_time`,
      type: `time`
    }
  },
  
  dataSource: `default`
});
