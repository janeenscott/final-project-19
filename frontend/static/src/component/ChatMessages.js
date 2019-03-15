import React, {Component} from 'react';

class ChatMessages extends Component {
    render() {
        return (
            <ul className='message-list'>
                {this.props.messages.map(message => {
                    return (
                        <li key={message.id}>
                            <div>
                                {message.sender}
                            </div>
                            <div>
                                {message.messageText}
                            </div>
                            <div>
                                {message.timeSent}
                            </div>
                        </li>
                    )
                })
                }
            </ul>
        )
    }
}

export default ChatMessages;