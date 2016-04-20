import React from 'react';
import QueryBar from './querybar';
import BodyInput from './bodyinput';

export default class Main extends React.Component {
	constructor() {
		super();
		this.state = {title: "", body: ""};

		this.getDocument = this.getDocument.bind(this);
		this.onBodyChange = this.onBodyChange.bind(this);
		this.onUpdateDocument = this.onUpdateDocument.bind(this);
	}
	onUpdateDocument() {
		console.log("Updating Document with body: " + this.state.body)
	}
	getDocument() {
		console.log("Fetching Document with title: " + this.state.title)
	}
	onBodyChange(body){
		this.setState({body})
	}
	render() {
		return (
			<div className="main col-md-offset-3 col-md-6">
				<div className="row padding-top">
					<QueryBar />
				</div>
				<BodyInput
					doc={this.state}
					onUpdateDocument={this.onUpdateDocument}
					onBodyChange={this.onBodyChange} />
			</div>
		)
	}
}