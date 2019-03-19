import React, {Component} from 'react';
import '../container/App.css';
import {stateToHTML} from 'draft-js-export-html';
import { convertFromRaw } from 'draft-js';


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
        try {
            var x = stateToHTML(convertFromRaw(JSON.parse(text)));
        }catch (e) {
            var x = text;
        }
        return x
    };

    render() {
        return (
            <ul className='message-list'>
                {this.props.messages.map(message => {
                    return (
                        <li key={message.id}>
                            <div>
                                {message.sender['first_name']}
                            </div>
                                <div
                                    dangerouslySetInnerHTML={{__html: this.convertMessageFromJSONToText(message['message_text'])}}>
                                </div>
                            <div>
                                {message['time_sent']}
                            </div>
                            <br/>
                        </li>
                    )
                })
                }
            </ul>
        )
    }
}

export default ChatMessages;