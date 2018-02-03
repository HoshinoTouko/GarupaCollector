import React from 'react';
import './App.css';
import AppLayout from "./Pages/Layout/Layout";

import zhCN from 'antd/lib/locale-provider/zh_CN';
import moment from 'moment';
import 'moment/locale/zh-cn';

moment.locale('zh-cn');

class App extends React.Component {
    render() {
        return (
            <div className="App">
                <AppLayout/>
            </div>
        );
    }
}

export default App;
