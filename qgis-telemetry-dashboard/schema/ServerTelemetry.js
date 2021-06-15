cube(`ServerTelemetry`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_telemetry`,
  
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
