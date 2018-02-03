/*
 * @File: Sider.jsx
 * @Author: HoshinoTouko
 * @License: (C) Copyright 2014 - 2017, HoshinoTouko
 * @Contact: i@insky.jp
 * @Website: https://touko.moe/
 * @Create at: 2018/2/3 22:03
 * @Desc: 
 */
import {Layout, Menu, Breadcrumb, Icon} from 'antd';
import React from 'react';

const {Header, Content, Footer, Sider} = Layout;
const SubMenu = Menu.SubMenu;

class AppSider extends React.Component {
    state = {
        collapsed: false,
    };
    onCollapse = (collapsed) => {
        console.log(collapsed);
        this.setState({collapsed});
    };

    render() {
        return (
            <Sider
                collapsible
                collapsed={this.state.collapsed}
                onCollapse={this.onCollapse}
            >
                <div style={logoStyle} className="logo"/>
                <Menu theme="dark" defaultSelectedKeys={['1']} mode="inline">
                    <Menu.Item key="1">
                        <Icon type="pie-chart"/>
                        <span>首页</span>
                    </Menu.Item>

                    <Menu.Item key="2">
                        <Icon type="pie-chart"/>
                        <span>总览</span>
                    </Menu.Item>

                    <Menu.Item key="3">
                        <Icon type="file"/>
                        <span>关于</span>
                    </Menu.Item>
                </Menu>
            </Sider>
        );
    }
}

let logoStyle = {
    height: '32px',
    background: 'rgba(255,255,255,.2)',
    margin: '16px',
};

export default AppSider;
