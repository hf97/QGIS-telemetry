cube(`ServerAction`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_action`,
  
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
    }
  },
  
  dataSource: `default`
});
