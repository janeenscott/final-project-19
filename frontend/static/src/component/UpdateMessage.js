import React, {Component} from 'react';
import '../container/App.css';
import {EditorState, ContentState, convertFromRaw, convertFromHTML} from "draft-js";
import {Editor} from "react-draft-wysiwyg";
import {stateToHTML} from "draft-js-export-html";

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

        let plainText;

        try {
            plainText = stateToHTML(convertFromRaw(JSON.parse(this.props.message.message_text)));
        } catch (e) {
            plainText = stateToHTML(convertFromRaw(this.props.message.message_text));

        }

        let blocksFromHTML = convertFromHTML(plainText);
        let editorState = ContentState.createFromBlockArray(
            blocksFromHTML.contentBlocks,
            blocksFromHTML.entityMap
        );


        editorState = EditorState.createWithContent(editorState);
        this.setState({
            editorState
        });
    }

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
                <div className="editor">
                    <Editor
                        editorState={this.state.editorState}
                        onEditorStateChange={this.onEditorStateChange}
                        // onChange={this.onChange}
                        toolbarClassName="toolbarClassName"
                        wrapperClassName="wrapperClassName"
                        editorClassName="editorClassName"
                    />
                </div>

                <button type="submit" className="btn btn-redirect">
                    Save
                </button>
            </form>
        )
    }
}

export default UpdateMessage;