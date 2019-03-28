import React, {Component} from 'react';
import '../container/App.css';
import {convertToRaw, EditorState, ContentState, convertFromRaw} from "draft-js";
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
        // console.log('what is here', this.props.message.message_text);

        // need try...catch because second update is throwing an error.
        // after edit the object is stored differently so it can't be edited again

        // let plainText;
        //     try {
        //         plainText = stateToHTML(convertFromRaw(JSON.parse(text)));
        //         console.log('try plainText :', plainText);
        //     }catch(e){
        //         plainText = stateToHTML(convertFromRaw(text));
        //         console.log('catch plainText :', plainText);
        //     }
        // console.log('plainText :', plainText);
        //  return plainText;

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