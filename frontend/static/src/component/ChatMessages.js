import React, {Component} from 'react';
import '../container/App.css';

class ChatMessages extends Component {
    // constructor(props) {
    //     super(props);
    //     this.state = {
    //         messages:  [
    //             {messageText: '', sender: '', timeSent: ''},
    //             ]
    //     }
    // }
    // getMessage = (message) => {
    //
    // }

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