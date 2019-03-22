import React, { Component } from 'react';
import './App.css';
import ChatMessages from  '../component/ChatMessages'
import ChatInput from  '../component/ChatInput'
import { convertFromRaw, convertToRaw } from 'draft-js';
import {stateToHTML} from 'draft-js-export-html';
import moment from 'moment'
import RedirectButton from "../component/RedirectButton";



class App extends Component {
    constructor(props){
        super(props);
        this.state = {
            messages: [
                // {messageText: '', sender: '', timeSent: ''},
                // {messageText: "What's up?", sender: 'Kelsey', timeSent: '12:02pm'},
                // {messageText: "Nothing. Just missing you and Hashbrown, wondering what you ladies are up to.", sender: 'Janeen', timeSent: '12:02pm'},
                // {messageText: "Girl, we're just both eating tomatoes, you're not missing much.", sender: 'Kelsey', timeSent: '12:03pm'}
                ]
            // only need message text in state
        };
        this.sendMessage = this.sendMessage.bind(this)
    }



    sendMessage = (editorState) => {
        var body = {
            message_text: convertToRaw(editorState.getCurrentContent())
        };
        console.log('body: ', body);
        console.log('editorState: ', editorState);

        fetch('/api/message/', {
            method: "POST",
            body: JSON.stringify(body),
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
        }).then((response) => {
            return response.json()
        }).then((post) => {
            var messages = this.state.messages;

            post.message_text = JSON.stringify(post.message_text);

            messages.push(post);

            this.setState({messages: messages})

            console.log('this: ', this.state.messages[messages.length-1]);
        });



    };


// loads messages from api/message onto screen
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
              {/*<h3>Not sure what to say?</h3>*/}
              {/*<ul>*/}
                  {/*<li className="topic">Convo topic #1</li>*/}
                  {/*<li className="topic">Convo topic #2</li>*/}
                  {/*<li className="topic">Convo topic #3</li>*/}
                  {/*<li className="topic">Convo topic #4</li>*/}
              {/*</ul>*/}
              <ChatMessages messages={this.state.messages}/>
              <ChatInput sendMessage={this.sendMessage}/>
              {/*<RedirectButton/>*/}
          </div>
        );
  }
}

export default App;
