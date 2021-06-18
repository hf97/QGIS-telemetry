cube(`ServerUiTheme`, {
  sql: `SELECT * FROM public.server_ui_theme`,
  
  preAggregations: {
    // Pre-Aggregations definitions go here
    // Learn more here: https://cube.dev/docs/caching/pre-aggregations/getting-started  
  },
  
  joins: {
    
  },
  
  measures: {
    count: {
      type: `count`,
      drillMembers: [name],
      title:`Ui themes`,
    }
  },
  segments:{
    notNull:{
      sql: `${CUBE}.name!='Null'`,
    }
  },
  
  dimensions: {
    ui_theme_id: {
      sql: `ui_theme_id`,
      type: `number`,
      primaryKey: true
    },
    name: {
      sql: `name`,
      type: `string`,
    },
  },
  
  dataSource: `default`
});
