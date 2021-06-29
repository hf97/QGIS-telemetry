import React from 'react';
import { Col } from 'antd';
import ChartRenderer from '../components/ChartRenderer';
import Dashboard from '../components/Dashboard';
import DashboardItem from '../components/DashboardItem';
const DashboardItems = [
  {
    id: 0,
    name: 'Ui themes',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCount'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.totalCount': 'desc',
        },
        filters: [],
        dimensions: ['ServerUiTheme.name'],
        segments: ['ServerUiTheme.notNull'],
      },
      chartType: 'bar',
    },
  },
  {
    id: 1,
    name: 'Plugins',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCountPlugin'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.dateTime': 'asc',
        },
        filters: [],
        dimensions: ['ServerPlugin.name'],
        segments: ['ServerPlugin.notNull'],
      },
      chartType: 'bar',
    },
  },
  {
    id: 2,
    name: 'Plugins Version',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCountPlugin'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.dateTime': 'asc',
        },
        filters: [],
        dimensions: ['ServerPlugin.name', 'ServerPlugin.version'],
        segments: ['ServerPlugin.notNull'],
      },
      chartType: 'bar',
    },
  },
  {
    id: 3,
    name: 'Server Protocols',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCountServer'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.dateTime': 'asc',
        },
        filters: [],
        dimensions: ['ServerServer.protocol'],
        segments: ['ServerServer.notNull'],
      },
      chartType: 'bar',
    },
  },
  {
    id: 4,
    name: 'Languages',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCountLanguage'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.dateTime': 'asc',
        },
        filters: [],
        dimensions: ['ServerLanguage.name'],
        segments: ['ServerLanguage.notNull'],
      },
      chartType: 'bar',
    },
  },
  {
    id: 5,
    name: 'Versions',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCountQgisVersion'],
        timeDimensions: [],
        order: [['ServerTelemetry.totalCountQgisVersion', 'asc']],
        filters: [],
        dimensions: ['ServerQgisVersion.name'],
        segments: ['ServerQgisVersion.notNull'],
      },
      chartType: 'bar',
    },
  },
  {
    id: 6,
    name: 'Locales',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCountLocale'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.dateTime': 'asc',
        },
        filters: [],
        dimensions: ['ServerLocale.name'],
        segments: ['ServerLocale.notNull'],
      },
      chartType: 'bar',
    },
  },
  {
    id: 7,
    name: 'Operative Systems',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCountOs'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.dateTime': 'asc',
        },
        filters: [],
        dimensions: ['ServerOs.name'],
        segments: ['ServerOs.notNull'],
      },
      chartType: 'bar',
    },
  },
  {
    id: 8,
    name: 'Most Used Actions',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCountActions'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.totalCountActions': 'desc',
        },
        filters: [],
        dimensions: ['ServerAction.name'],
        segments: [],
      },
      chartType: 'bar',
    },
  },
  {
    id: 9,
    name: 'Map Layers',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalCountlayers'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.totalCountlayers': 'desc',
        },
        filters: [],
        dimensions: ['ServerAddedLayer.name'],
        segments: ['ServerAddedLayer.notNull'],
      },
      chartType: 'bar',
    },
  },
  {
    id: 10,
    name: 'Telemetry by Locations',
    vizState: {
      query: {
        measures: ['ServerTelemetry.totalLocation'],
        timeDimensions: [],
        order: {
          'ServerTelemetry.totalLocation': 'desc',
        },
        filters: [],
        dimensions: ['ServerLocation.name'],
        segments: ['ServerLocation.notNull'],
      },
      chartType: 'bar',
    },
  },
];

const DashboardPage = () => {
  const dashboardItem = (item) => (
    <Col
      span={24}
      lg={12}
      key={item.id}
      style={{
        marginBottom: '24px',
      }}
    >
      <DashboardItem title={item.name}>
        <ChartRenderer vizState={item.vizState} />
      </DashboardItem>
    </Col>
  );

  const Empty = () => (
    <div
      style={{
        textAlign: 'center',
        padding: 12,
      }}
    >
      <h2>
        There are no charts on this dashboard. Use Playground Build to add one.
      </h2>
    </div>
  );

  return DashboardItems.length ? (
    <Dashboard dashboardItems={DashboardItems}>
      {DashboardItems.map(dashboardItem)}
    </Dashboard>
  ) : (
    <Empty />
  );
};

export default DashboardPage;
