cube(`ServerLocale`, {
  sql: `SELECT * FROM "qgis-telemetry-schema".server_locale`,
  
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
    locale_id: {
      sql: `locale_id`,
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