import React from 'react';
import { Link } from 'react-router-dom';
import { withRouter } from 'react-router';
import { Layout, Menu } from 'antd';

const Header = ({ location }) => (
  <Layout.Header
    style={{
      padding: '0 32px',
      backgroundColor: '#6a8d25',
    }}
  >
    <div
      style={{
        float: 'left',
      }}
    >
      <h2
        style={{
          color: '#fff',
          margin: 0,
          marginRight: '1em',
          display: 'inline',
          width: 100,
          lineHeight: '54px',
        }}
      >
        QGIS Telemetry Dashboard
      </h2>
    </div>
    <Menu
      theme="dark"
      mode="horizontal"
      selectedKeys={[location.pathname]}
      style={{
        lineHeight: '64px',
      }}
    >
    </Menu>
  </Layout.Header>
);

export default withRouter(Header);
