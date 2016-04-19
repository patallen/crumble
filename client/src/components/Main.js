import React from 'react';
import QueryBar from './querybar';


export default class Main extends React.Component {
	constructor() {
		super();
		this.state = {title: "", body: ""};

		this.updateDocument = this.updateDocument.bind(this);
		this.getDocument = this.getDocument.bind(this);
		this.handleBody = this.handleBody.bind(this);
	}
	updateDocument() {
		console.log("Updating Document with body: " + this.state.body)
	}
	getDocument() {
		console.log("Fetching Document with title: " + this.state.title)
	}
	handleBody(event) {
		this.setState({body: event.target.value})
	}
	render() {
		return (
			<div className="main col-md-offset-3 col-md-6">
				<div className="row padding-top">
					<QueryBar />
				</div>
				<div className="row padding-top">
					<div className="col-xs-12">
						<textarea className="form-control" rows="20" defaultValue={this.state.body} onChange={this.handleBody}></textarea>
					</div>
				</div>
				<div className="row padding-top">
					<div className="col-xs-12">
						<button className="btn btn-success btn-block" onClick={this.updateDocument}>Update</button>
					</div>
				</div>
			</div>
		)
	}
}