import React, { Component } from 'react';
import './App.css';
import ChatMessages from  '../component/ChatMessages'
import ChatInput from  '../component/ChatInput'
import moment from 'moment'



class App extends Component {
    constructor(props){
        super(props);
        this.state = {
            currentUser: '',
            messages: [
                {messageText: 'Heyyyy', sender: 'Janeen', timeSent: '12:01pm'},
                {messageText: "What's up?", sender: 'Kelsey', timeSent: '12:02pm'},
                {messageText: "Nothing. Just missing you and Hashbrown, wondering what you ladies are up to.", sender: 'Janeen', timeSent: '12:02pm'},
                {messageText: "Girl, we're just both eating tomatoes, you're not missing much.", sender: 'Kelsey', timeSent: '12:03pm'}
                ]
        };
        this.sendMessage = this.sendMessage.bind(this)
    }
    sendMessage = (message) =>{
        const messages = this.state.messages;
        messages.push({
            messageText: message,
            sender: this.state.currentUser,
            timeSent: moment(message['date']).format('MMMM Do, h:mm a')
        });
        this.setState({messages: messages})
        // console.log('this: ', this.state.messages[0]);

    };


  render() {
    return (
      <div className="App">
          <h1>Let's talk!</h1>

          <ChatMessages messages={this.state.messages}/>
          <ChatInput sendMessage={this.sendMessage}/>
      </div>
    );
  }
}

export default App;
