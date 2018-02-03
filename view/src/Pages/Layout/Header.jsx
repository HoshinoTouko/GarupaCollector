/*
 * Created with Web Storm.
 * @File: Header.jsx
 * @Author: Hoshino Touko
 * @License: (C) Copyright 2014 - 2017, HoshinoTouko
 * @Contact: i@insky.jp
 * @Website: https://touko.moe/
 * @Create at: 2018/2/3 22:14
 * @Desc: 
 */


import {Layout, Menu, Breadcrumb, Icon} from 'antd';
import React from 'react';

const {Header, Content, Footer, Sider} = Layout;
const SubMenu = Menu.SubMenu;

class AppHeader extends React.Component {
    render() {
        return (
            <Header style={{background: '#fff', paddingLeft: 40}}>
                <h3>Garupa Collector</h3>
            </Header>
        );
    }
}

export default AppHeader;
