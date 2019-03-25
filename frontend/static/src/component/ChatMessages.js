import React, {Component} from 'react';
import '../container/App.css';
import {stateToHTML} from 'draft-js-export-html';
import {convertFromRaw, EditorState} from 'draft-js';
import Listgroup from 'react-bootstrap/ListGroup'


import moment from 'moment'


class ChatMessages extends Component {
    constructor(props) {
        super(props);
        this.state = {
            // messages:  [
            //     {messageText: '', sender: '', timeSent: ''},
            //     ]
        }

    }

    convertMessageFromJSONToText = (text) => {
        let x;

        try {
            x = stateToHTML(convertFromRaw(JSON.parse(text)));
            console.log('try', x);
        } catch (e) {
            x = text.blocks[0].text;
            console.log('catch', x);
        }

        console.log('what are we returning', x);
        return x
    };


    render() {
        return (
            <div className='message-list'>
                {this.props.messages.map(message => {
                    return (
                        <Listgroup className="message" key={message.id}>
                            <Listgroup.Item>
                                {message.sender['first_name']}
                            </Listgroup.Item>
                            <Listgroup.Item
                                dangerouslySetInnerHTML={{__html: this.convertMessageFromJSONToText(message['message_text'])}}>
                            </Listgroup.Item>
                            <Listgroup.Item>
                                {message['time_sent']}
                            </Listgroup.Item>
                            <Listgroup.Item>

                                <p className='edit' onClick={() => this.props.handleEdit(message)}>&#9998;</p>
                                <p className='delete' onClick={() => this.props.deleteMessage(message)}>🗑️</p>
                            </Listgroup.Item>

                            <br/>
                        </Listgroup>
                    )
                })
                }
            </div>
        )
    }
}

export default ChatMessages;