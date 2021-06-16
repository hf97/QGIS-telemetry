cube(`ServerAction`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_action`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    ServerInterface: {
      relationship: `hasOne`,
      sql: `${ServerAction}.interface_id = ${ServerInterface}.interface_id`,
    }
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [name, dateTime]
    },
    actionUICount:{
      sql: `${count2}`,
      type:`sum`
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
    },
    count2: {
      sql: `${ServerInterface.uiCount}`,
      type: `number`,
      subQuery: true
    }
  },
  
  dataSource: `default`
});
