import React, { Component } from 'react';
import './App.css';
import ChatMessages from  '../component/ChatMessages'
import ChatInput from  '../component/ChatInput'
import moment from 'moment'



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
            // only need message text in state
        };
        this.sendMessage = this.sendMessage.bind(this)
    }
    sendMessage = (message) =>{
        const messages = this.state.messages;
        console.log('messages ', messages);
        fetch('api/message/', {
            method: "POST",
            body: JSON.stringify(message),
        })
            .then(response => response.json());
        messages.push({
            messageText: message,
            sender: this.messages.sender,
            timeSent: moment(message['date']).format('MMMM Do, h:mm a')
        });
        this.setState({messages: messages})
        // console.log('this: ', this.state.messages[0]);

    };

    componentDidMount() {
        fetch('/api/message/')
            .then(res => res.json())
            .then(
                (result) => {
                    console.log(result)
            this.setState({
                messages: result
            });
        },
                (error) =>{
                    this.setState({
                        error
                    });
                }

            )
    }

    render() {
    return (
      <div className="App">
          <h1>Let's talk!</h1>
          <h3>Not sure what to say?</h3>
          <ul>
              <li className="topic">Convo topic #1</li>
              <li className="topic">Convo topic #2</li>
              <li className="topic">Convo topic #3</li>
              <li className="topic">Convo topic #4</li>
          </ul>

          <ChatMessages messages={this.state.messages}/>
          <ChatInput sendMessage={this.sendMessage}/>
      </div>
    );
  }
}

export default App;
