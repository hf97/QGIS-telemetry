cube(`ServerTelemetry`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_telemetry`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    ServerAction: {
      relationship: `hasMany`,
      sql: `${ServerTelemetry}.telemetry_id = ${ServerAction}.telemetry_id`,
    }
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [dateTime]
    },
    totalCount: {
      sql:`${count2}`,
      type:`sum`
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
    },
    count2: {
      sql: `${ServerAction.actionUICount}`,
      type: `number`,
      subQuery: true
    }
  },
  
  dataSource: `default`
});
