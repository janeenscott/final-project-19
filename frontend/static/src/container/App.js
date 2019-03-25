import React, {Component} from 'react';
import './App.css';
import ChatMessages from '../component/ChatMessages'
import ChatInput from '../component/ChatInput'
import {convertFromRaw, convertToRaw, EditorState} from 'draft-js';
import {stateToHTML} from 'draft-js-export-html';
import moment from 'moment'
import UpdateMessage from "../component/UpdateMessage";
import Button from 'react-bootstrap/Button'


class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            messages: [],
            isEditing: false,
        };

        this.sendMessage = this.sendMessage.bind(this);
        this.handleEdit = this.handleEdit.bind(this);
        // this.handleDelete = this.handleDelete.bind(this);
    }

    //************ API methods *********

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

            this.setState({messages: messages});

            console.log('this: ', this.state.messages[messages.length - 1]);
        });


    };

    updateMessage = (editorState) => {
        var body = {
            message_text: convertToRaw(editorState.getCurrentContent())
        };
        console.log('updateMessage, body: ', body);
        console.log('updateMessage, editorState: ', editorState);

        fetch(`/api/message/${this.state.isEditing.id}/`, {
            method: "PATCH",
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


            console.log('body: ', body);
            console.log('editorState: ', editorState);
            this.setState({messages: messages, isEditing: false});

            console.log('new state, last message ', this.state.messages[messages.length - 1]);
        });


    };

    deleteMessage = (message) => {
        console.log('message: ', message);
        fetch(`/api/message/delete/${message.id}/`, {
            method: "DELETE",
            },
        )
            .then(response => {
              console.log(response);
            },
            )
            .then((messages) => {
                let allMessages = this.state.messages;
                let newMessages = allMessages.filter((currentMessage) => {
                    return currentMessage.id !== message.id;
                });

                this.setState({messages: newMessages})
                }
            )
    };


    //******* Handlers **********

    handleEdit(message) {

        console.log('handleEdit is firing', message);
        this.setState({isEditing: message});

    }



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
                (error) => {
                    this.setState({
                        error
                    });
                }
            )
    }

    render() {
        const isEditing = this.state.isEditing;

        return (
            <div className="App">
                 <button>
                    <a href="../profile">Go Back to Profile</a>
                </button>
                <h1>Let's talk!</h1>
                {/*<h3>Not sure what to say?</h3>*/}
                {/*<ul>*/}
                {/*<li className="topic">Convo topic #1</li>*/}
                {/*<li className="topic">Convo topic #2</li>*/}
                {/*<li className="topic">Convo topic #3</li>*/}
                {/*<li className="topic">Convo topic #4</li>*/}
                {/*</ul>*/}


                {isEditing ? (
                    <UpdateMessage updateMessage={this.updateMessage} message={this.state.isEditing}/>
                ) : (
                    <div>
                        <ChatMessages messages={this.state.messages} deleteMessage={this.deleteMessage} handleEdit={this.handleEdit}/>
                        <ChatInput sendMessage={this.sendMessage}/>
                    </div>
                )
                }
                {/*<Button onClick={location.href='buddies:profile'}/>*/}


            </div>
        );
    }
}

export default App;
