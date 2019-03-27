import React, {Component} from 'react';
import '../container/App.css';
import {stateToHTML} from 'draft-js-export-html';
import {convertFromRaw, EditorState} from 'draft-js';
import Listgroup from 'react-bootstrap/ListGroup'


import Moment from 'react-moment';


class ChatMessages extends Component {
    constructor(props) {
        super(props);
        this.state = {
            // userAuthorized: false
        };

        // const moment = require('moment');
        //
        // let now = moment();


    }

    // hideIfUnauthorized = (user) =>{
    //     if (user = self.request.user);
    //     {userAuthorized: true}
    // };


    convertMessageFromJSONToText = (text) => {
        console.log('this is my text', text);
        let x;

        try {
            // this fires when you add a new message
            x = stateToHTML(convertFromRaw(JSON.parse(text)));
            console.log('try', x);
        } catch (e) {
            // x = stateToHTML(convertFromRaw(text));
            // this fires when you pull data from the server
            x = text.blocks[0].text;
            console.log('catch me here', x);
        }

        console.log('what are we returning', x);
        return x
    };


    render() {

        return (
            <div className='message-list'>
                <div>
                    {this.props.messages.map(message => {
                        const dateToFormat = message['time_sent'];
                        return (

                                <Listgroup className="message" key={message.id}>
                                    <Listgroup.Item>
                                        {message.sender['first_name']}
                                    </Listgroup.Item>
                                    <Listgroup.Item
                                        dangerouslySetInnerHTML={{__html: this.convertMessageFromJSONToText(message['message_text'])}}>
                                    </Listgroup.Item>
                                    <Listgroup.Item>
                                        <Moment format="MMMM Do YYYY, h:mm a">
                                            {dateToFormat}
                                        </Moment>
                                    </Listgroup.Item>

                                    <Listgroup.Item className="unauthorized">
                                        <p className='edit' onClick={() => this.props.handleEdit(message)}>&#9998;</p>
                                        <p className='delete' onClick={() => this.props.deleteMessage(message)}>🗑️</p>
                                    </Listgroup.Item>
                                    <br/>
                                </Listgroup>


                        )
                    })
                    }
                     </div>
                </div>
                )
                }
                }

                export default ChatMessages;