cube(`ServerPlugin`, {
  sql: `SELECT * FROM public.server_plugin`,
  
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
  segments:{
    notNull:{
      sql: `${CUBE}.name!='Null'`,
    }},
  
  dimensions: {
    plugin_id: {
      sql: `plugin_id`,
      type: `number`,
      primaryKey: true
    },
    
    name: {
      sql: `name`,
      type: `string`
    },
    
    version: {
      sql: `version`,
      type: `string`
    }
  },
  
  dataSource: `default`
});
