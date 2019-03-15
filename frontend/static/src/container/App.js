import React, { Component } from 'react';
import './App.css';
import ChatMessages from  '../component/ChatMessages'


class App extends Component {
    constructor(props){
        super(props);
        this.state = {
            messages: [
                {messageText: 'Heyyyy', sender: 'Janeen', timeSent: '12:01pm'},
                {messageText: "What's up?", sender: 'Kelsey', timeSent: '12:02pm'},
                {messageText: "Nothing. Just missing you and Hashbrown, wondering what you ladies are up to.", sender: 'Janeen', timeSent: '12:02pm'},
                {messageText: "Girl, we're just both eating tomatoes, you're not missing much.", sender: 'Kelsey', timeSent: '12:03pm'}
                ]
        }
    }
  render() {
    return (
      <div className="App">
          <h1>Let's talk!</h1>

          <ChatMessages messages={this.state.messages}/>
          {/*<ChatInput/>*/}
      </div>
    );
  }
}

export default App;
