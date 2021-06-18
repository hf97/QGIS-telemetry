cube(`ServerAddedLayer`, {
  sql: `SELECT * FROM public.server_added_layer`,
  
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
  segments:{
    notNull:{
      sql: `${CUBE}.name!='Null'`,
    }
  },
  
  dimensions: {
    added_layer_id: {
      sql: `added_layer_id`,
      type: `number`,
      primaryKey: true
    },
    
    name: {
      sql: `name`,
      type: `string`
    },
    
    extension: {
      sql: `extension`,
      type: `string`
    },
    
    dateTime: {
      sql: `date_time`,
      type: `time`
    }
  },
  
  dataSource: `default`
});
