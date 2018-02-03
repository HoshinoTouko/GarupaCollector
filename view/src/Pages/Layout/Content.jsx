/*
 * Created with Web Storm.
 * @File: Content.jsx
 * @Author: Hoshino Touko
 * @License: (C) Copyright 2014 - 2017, HoshinoTouko
 * @Contact: i@insky.jp
 * @Website: https://touko.moe/
 * @Create at: 2018/2/3 22:22
 * @Desc: 
 */
import { Layout, Menu, Breadcrumb, Icon } from 'antd';
import React from 'react';
import {HashRouter as Router, Route, Redirect, Switch} from 'react-router-dom';
import MainPage from "../Pages/MainPage";

const { Header, Content, Footer, Sider } = Layout;
const SubMenu = Menu.SubMenu;

class AppContent extends React.Component{
    render(){
        return(
            <Content style={{ margin: '0 16px' }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item>User</Breadcrumb.Item>
                    <Breadcrumb.Item>Bill</Breadcrumb.Item>
                </Breadcrumb>
                <div style={{ padding: 24, background: '#fff', minHeight: 360 }}>
                    <Router>
                        <Switch>
                            <Route exact path="/" component={MainPage}/>
                        </Switch>
                    </Router>
                </div>
            </Content>
        )
    }
}

export default AppContent;
