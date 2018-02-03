/*
 * Created with Web Storm.
 * @File: MainPage.jsx
 * @Author: Hoshino Touko
 * @License: (C) Copyright 2014 - 2017, HoshinoTouko
 * @Contact: i@insky.jp
 * @Website: https://touko.moe/
 * @Create at: 2018/2/3 23:09
 * @Desc: 
 */
import React from 'react';
import { Table } from 'antd';
import reqwest from 'reqwest';
import { List, Avatar, Icon } from 'antd';

class MainPage extends React.Component {
    state = {
        data: [],
        loading: true,
    };
    pagination= {
        pageSize: 10,
        defaultCurrent: 1,
        total: 20,
        onChange: (page) => {
            this.pagination.current = page;
            window.scrollTo(0, 0);
            this.fetch();
        },
    };
    fetch = () => {
        this.setState({ loading: true });
        reqwest({
            url: 'http://localhost:5000/public/data/all',
            method: 'get',
            data: {
                num: 10,
                page: this.pagination.current
            },
        }).then((strData) => {
            let data = JSON.parse(strData);

            this.pagination.total = data.total;
            console.log(data.result);
            this.setState({
                loading: false,
                data: data.result
            });
        });

    };
    componentDidMount() {
        this.fetch();
    }
    render() {
        return (
            <List
                itemLayout="vertical"
                size="large"
                pagination={this.pagination}
                dataSource={this.state.data}
                renderItem={item => (
                    <List.Item
                        key={item.id}
                        actions={[<IconText type="star-o" text="156" />, <IconText type="like-o" text="156" />, <IconText type="message" text="2" />]}
                        extra={<img width={272} alt="logo" src={item.titleImg} />}
                    >
                        <List.Item.Meta
                            title={<a href={null}>{item.title}</a>}
                            description={item.desc}
                        />
                        <div>
                            {item.content.slice(0, 80) + '......'}
                        </div>
                    </List.Item>
                )}
            />
        );
    }
}

const IconText = ({ type, text }) => (
    <span>
    <Icon type={type} style={{ marginRight: 8 }} />
        {text}
  </span>
);

export default MainPage;
