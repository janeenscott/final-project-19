import React, {Component} from 'react';
import '../container/App.css';
import { EditorState, convertFromRaw, convertToRaw } from 'draft-js';
import {Editor} from 'react-draft-wysiwyg'
import 'react-draft-wysiwyg/dist/react-draft-wysiwyg.css';


class ChatInput extends Component{
    constructor(props){
        super(props);
        this.state = {
            messageText: '',
            editorState: EditorState.createEmpty()
        };
        // this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);

    }

    // handleChange(event){
    //     this.setState({
    //         [event.target.name]: event.target.value
    //     })
    // }

    onEditorStateChange = (editorState) => {
        this.setState({
            editorState,
        });
    };

    handleSubmit(event){
        event.preventDefault();
        convertToRaw(this.state.editorState.getCurrentContent());
        this.props.sendMessage(this.state.editorState);
        this.setState({
            editorState: EditorState.createEmpty()

            // messageText: ''
        })
    }

    render() {
        return(
         <form
             className='message-input-form'
             onSubmit={this.handleSubmit}
         >

               <Editor
                editorState={this.state.editorState}
                toolbarClassName="toolbarClassName"
                wrapperClassName="wrapperClassName"
                editorClassName="editorClassName"
                onEditorStateChange={this.onEditorStateChange}
            />
             {/*<textarea*/}
                 {/*cols={40}*/}
                 {/*rows={10}*/}
                 {/*name='messageText'*/}
                 {/*onChange={this.handleChange}*/}
                 {/*value={this.state.messageText}*/}
                 {/*placeholder='Type your message here'*/}
             {/*/>*/}
              <button type="submit" className="btn btn-primary">
                        Send
                    </button>
         </form>
        )
    }
}

export default ChatInput;