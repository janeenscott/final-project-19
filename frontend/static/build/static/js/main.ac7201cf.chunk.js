(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{207:function(e,t,a){"use strict";a.r(t);var s=a(0),n=a.n(s),o=a(23),i=a.n(o),r=(a(94),a(16)),c=a(17),l=a(19),m=a(18),d=a(20),u=a(8),g=(a(32),a(56)),h=a(4),p=a(26),b=a.n(p),S=a(88),f=a.n(S),E=function(e){function t(e){var a;return Object(r.a)(this,t),(a=Object(l.a)(this,Object(m.a)(t).call(this,e))).convertMessageFromJSONToText=function(e){var t;console.log("this is my text",e);try{t=Object(g.stateToHTML)(Object(h.convertFromRaw)(JSON.parse(e))),console.log("try",t)}catch(a){t=e.blocks[0].text,console.log("catch me here",t)}return console.log("what are we returning",t),t},a.state={},a}return Object(d.a)(t,e),Object(c.a)(t,[{key:"render",value:function(){var e=this;return n.a.createElement("div",{className:"message-list"},this.props.messages.map(function(t){var a=t.time_sent;return n.a.createElement(b.a,{className:"message",key:t.id},n.a.createElement(b.a.Item,null,t.sender.first_name),n.a.createElement(b.a.Item,{dangerouslySetInnerHTML:{__html:e.convertMessageFromJSONToText(t.message_text)}}),n.a.createElement(b.a.Item,null,n.a.createElement(f.a,null,a)),n.a.createElement(b.a.Item,{className:"unauthorized"},n.a.createElement("p",{className:"edit",onClick:function(){return e.props.handleEdit(t)}},"\u270e"),n.a.createElement("p",{className:"delete",onClick:function(){return e.props.deleteMessage(t)}},"\ud83d\uddd1\ufe0f")),n.a.createElement("br",null))}))}}]),t}(s.Component),v=a(38),O=(a(206),function(e){function t(e){var a;return Object(r.a)(this,t),(a=Object(l.a)(this,Object(m.a)(t).call(this,e))).onEditorStateChange=function(e){a.setState({editorState:e})},a.state={messageText:"",editorState:h.EditorState.createEmpty()},a.handleSubmit=a.handleSubmit.bind(Object(u.a)(Object(u.a)(a))),a}return Object(d.a)(t,e),Object(c.a)(t,[{key:"handleSubmit",value:function(e){e.preventDefault(),Object(h.convertToRaw)(this.state.editorState.getCurrentContent()),console.log("send message",this.state.editorState),this.props.sendMessage(this.state.editorState),this.setState({editorState:h.EditorState.createEmpty()})}},{key:"render",value:function(){return n.a.createElement("form",{className:"message-input-form",onSubmit:this.handleSubmit},n.a.createElement("div",{className:"editor"},n.a.createElement(v.Editor,{editorState:this.state.editorState,toolbarClassName:"toolbarClassName",wrapperClassName:"wrapperClassName",editorClassName:"editorClassName",onEditorStateChange:this.onEditorStateChange}),n.a.createElement("button",{type:"submit",className:"btn btn-redirect"},"Send")))}}]),t}(s.Component)),j=(a(83),function(e){function t(e){var a;return Object(r.a)(this,t),(a=Object(l.a)(this,Object(m.a)(t).call(this,e))).onEditorStateChange=function(e){console.log("editorState onEditorStateChange: ",e),a.setState({editorState:e})},a.state={messageText:"",editorState:null},a.handleSubmit=a.handleSubmit.bind(Object(u.a)(Object(u.a)(a))),a}return Object(d.a)(t,e),Object(c.a)(t,[{key:"componentDidMount",value:function(){var e=this.props.message.message_text.blocks[0].text,t=h.ContentState.createFromText(e),a=h.EditorState.createWithContent(t);a=h.EditorState.moveFocusToEnd(a),this.setState({editorState:a})}},{key:"handleSubmit",value:function(e){e.preventDefault(),console.log("editor state on submit: ",this.state.editorState),this.props.updateMessage(this.state.editorState),this.setState({editorState:h.EditorState.createEmpty()})}},{key:"render",value:function(){return console.log("editor state at top of render: ",this.state.editorState),n.a.createElement("form",{className:"message-input-form",onSubmit:this.handleSubmit},n.a.createElement(v.Editor,{editorState:this.state.editorState,onEditorStateChange:this.onEditorStateChange,toolbarClassName:"toolbarClassName",wrapperClassName:"wrapperClassName",editorClassName:"editorClassName"}),n.a.createElement("button",{type:"submit",className:"btn btn-primary"},"Save"))}}]),t}(s.Component)),C=function(e){function t(e){var a;return Object(r.a)(this,t),(a=Object(l.a)(this,Object(m.a)(t).call(this,e))).sendMessage=function(e){var t={message_text:Object(h.convertToRaw)(e.getCurrentContent())};console.log("body: ",t),console.log("editorState: ",e),fetch("/api/message/",{method:"POST",body:JSON.stringify(t),headers:{Accept:"application/json","Content-Type":"application/json"}}).then(function(e){return e.json()}).then(function(e){var t=a.state.messages;e.message_text=JSON.stringify(e.message_text),t.push(e),a.setState({messages:t}),console.log("this: ",a.state.messages[t.length-1])})},a.updateMessage=function(e){var t={message_text:Object(h.convertToRaw)(e.getCurrentContent())};console.log("updateMessage, body: ",t),console.log("updateMessage, editorState: ",e),fetch("/api/message/".concat(a.state.isEditing.id,"/"),{method:"PATCH",body:JSON.stringify(t),headers:{Accept:"application/json","Content-Type":"application/json"}}).then(function(e){return e.json()}).then(function(s){var n=a.state.messages;s.message_text=JSON.stringify(s.message_text),n.push(s),console.log("body: ",t),console.log("editorState: ",e),a.setState({messages:n}),console.log("new state, last message ",a.state.messages[n.length-1])})},a.deleteMessage=function(e){console.log("message: ",e),fetch("/api/message/delete/".concat(e.id,"/"),{method:"DELETE"}).then(function(e){console.log(e)}).then(function(t){var s=a.state.messages.filter(function(t){return t.id!==e.id});a.setState({messages:s})})},a.state={messages:[],isEditing:!1},a.sendMessage=a.sendMessage.bind(Object(u.a)(Object(u.a)(a))),a.handleEdit=a.handleEdit.bind(Object(u.a)(Object(u.a)(a))),a}return Object(d.a)(t,e),Object(c.a)(t,[{key:"handleEdit",value:function(e){console.log("handleEdit is firing",e),this.setState({isEditing:e})}},{key:"componentDidMount",value:function(){var e=this;fetch("/api/message/").then(function(e){return e.json()}).then(function(t){console.log(t),e.setState({messages:t})},function(t){e.setState({error:t})})}},{key:"render",value:function(){var e=this.state.isEditing;return n.a.createElement("div",{className:"App"},n.a.createElement("form",{action:"../profile"},n.a.createElement("button",{className:"btn-redirect"},"Go Back to Profile")),n.a.createElement("h1",null,"Let's talk!"),e?n.a.createElement(j,{updateMessage:this.updateMessage,message:this.state.isEditing}):n.a.createElement("div",null,n.a.createElement(E,{messages:this.state.messages,deleteMessage:this.deleteMessage,handleEdit:this.handleEdit}),n.a.createElement(O,{sendMessage:this.sendMessage})))}}]),t}(s.Component);Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));i.a.render(n.a.createElement(C,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})},32:function(e,t,a){},89:function(e,t,a){e.exports=a(207)},94:function(e,t,a){}},[[89,1,2]]]);
//# sourceMappingURL=main.ac7201cf.chunk.js.map