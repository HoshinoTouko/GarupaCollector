/*
 * Created with Web Storm.
 * @File: Layout.jsx
 * @Author: Hoshino Touko
 * @License: (C) Copyright 2014 - 2017, HoshinoTouko
 * @Contact: i@insky.jp
 * @Website: https://touko.moe/
 * @Create at: 2018/2/3 22:11
 * @Desc: 
 */

import { Layout, Menu, Breadcrumb, Icon } from 'antd';
import React from 'react';

import AppSider from "./Sider";
import AppHeader from "./Header";
import AppFooter from "./Footer";
import AppContent from "./Content";

const { Header, Content, Footer, Sider } = Layout;
const SubMenu = Menu.SubMenu;

class AppLayout extends React.Component{
    state = {
        collapsed: false,
    };
    onCollapse = (collapsed) => {
        console.log(collapsed);
        this.setState({ collapsed });
    };
    render() {
        return (
            <Layout style={{ minHeight: '100vh' }}>
                <AppSider/>
                <Layout>
                    <AppHeader/>
                    <AppContent/>
                    <AppFooter/>
                </Layout>
            </Layout>
        );
    }
}

export default AppLayout;
