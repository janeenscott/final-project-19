import React, {Component} from 'react';
import '../container/App.css';

class ChatInput extends Component{
    constructor(props){
        super(props);
        this.state = {
            messageText: ''
        };
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }

    handleChange(event){
        this.setState({
            messageText: event.target.value
        })
    }

    handleSubmit(event){
        event.preventDefault();
        this.props.sendMessage(this.state.messageText);
        this.setState({
            messageText: ''
        })
    }

    render() {
        return(
         <form
             className='message-input-form'
             onSubmit={this.handleSubmit}
         >
             <textarea
                 cols={40}
                 rows={10}
                 name='messageText'
                 onChange={this.handleChange}
                 value={this.state.messageText}
                 placeholder='Type your message here'
             />
              <button type="submit" className="btn btn-primary">
                        Send
                    </button>
         </form>
        )
    }
}

export default ChatInput;