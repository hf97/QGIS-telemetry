cube(`ServerLanguage`, {
  sql: `SELECT * FROM public.server_language`,
  
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
    language_id: {
      sql: `language_id`,
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
