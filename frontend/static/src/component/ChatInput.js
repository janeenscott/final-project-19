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
        console.log('send message', this.state.editorState);
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

             <div className='editor'>
               <Editor
                editorState={this.state.editorState}
                toolbarClassName="toolbarClassName"
                wrapperClassName="wrapperClassName"
                editorClassName="editorClassName"
                onEditorStateChange={this.onEditorStateChange}
            />
            </div>
              <button type="submit" className="btn btn-redirect">
                        Send
                    </button>

         </form>
        )
    }
}

export default ChatInput;