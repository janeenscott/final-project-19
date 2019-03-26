import React, {Component} from 'react';
import '../container/App.css';
import {convertToRaw, EditorState, ContentState} from "draft-js";
import {Editor} from "react-draft-wysiwyg";

class UpdateMessage extends Component {
    constructor(props) {
        super(props);
        // let plainText = 'What up dude'
        // let content = ContentState.createFromText(plainText);
        this.state = {
            // messageText: '',
            editorState: null
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        // this.onChange = this.onChange.bind(this);
    }


    componentDidMount() {
        let plainText = this.props.message.message_text.blocks[0].text;
        let content = ContentState.createFromText(plainText);
        let editorState = EditorState.createWithContent(content);
        editorState = EditorState.moveFocusToEnd(editorState);
        this.setState({
            editorState
        });
    }

    //  onChange(editorState) {
    //     console.log('onChange, editorState', editorState);
    //     // this.setState({editorState});
    // }

    onEditorStateChange = (editorState) => {
        console.log('editorState onEditorStateChange: ', editorState);
        // console.log(editorState.message.id)
        this.setState({editorState});
    };


    handleSubmit(event) {
        event.preventDefault();
        console.log('editor state on submit: ', this.state.editorState);
        // convertToRaw(this.state.editorState.getCurrentContent());
        // console.log('send message', this.state.editorState);
        this.props.updateMessage(this.state.editorState);
        this.setState({
            editorState: EditorState.createEmpty()
        })
    }

    render() {
        console.log('editor state at top of render: ', this.state.editorState);
        return (
            <form
                className='message-input-form'
                onSubmit={this.handleSubmit}
            >

                <Editor
                    editorState={this.state.editorState}
                    onEditorStateChange={this.onEditorStateChange}
                    // onChange={this.onChange}
                    toolbarClassName="toolbarClassName"
                    wrapperClassName="wrapperClassName"
                    editorClassName="editorClassName"
                />

                <button type="submit" className="btn btn-primary">
                    Save
                </button>
            </form>
        )
    }
}

export default UpdateMessage;