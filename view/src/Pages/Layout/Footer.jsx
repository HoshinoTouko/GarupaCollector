/*
 * Created with Web Storm.
 * @File: Footer.jsx
 * @Author: Hoshino Touko
 * @License: (C) Copyright 2014 - 2017, HoshinoTouko
 * @Contact: i@insky.jp
 * @Website: https://touko.moe/
 * @Create at: 2018/2/3 22:19
 * @Desc: 
 */
import {Layout, Menu, Breadcrumb, Icon} from 'antd';
import React from 'react';

const {Header, Content, Footer, Sider} = Layout;
const SubMenu = Menu.SubMenu;

class AppFooter extends React.Component{
    render(){
        return(
            <Footer style={{ textAlign: 'center' }}>
                Ant Design ©2016 Created by Ant UED
            </Footer>
        )
    }
}

export default AppFooter;
