import React from 'react';
import axios from 'axios';
import QueryBar from './querybar';
import BodyInput from './bodyinput';

const ax = axios.create({
  baseURL: 'http://localhost:5000/',
  timeout: 1000
});

export default class Main extends React.Component {
	constructor() {
		super();
		this.state = {title: "", body: ""};

		this.getDocument = this.getDocument.bind(this);
		this.onBodyChange = this.onBodyChange.bind(this);
		this.onUpdateDocument = this.onUpdateDocument.bind(this);
	}
	onUpdateDocument() {
		let title = this.state.title;
		let body = this.state.body;

		ax.post(`/public/document/${title}`, {body})
			.then(res => {})
			.catch(err => {console.log(err.data)})
	}
	getDocument(title) {
		let body;
		ax.get(`/public/document/${title}`)
			.then(res => {
				this.setState({title: res.data.title, body: res.data.body || ""});
			})
			.catch(err => {console.log(err)})
	}
	onBodyChange(body){
		this.setState({body})
	}
	render() {
		return (
			<div className="main col-md-offset-3 col-md-6">
				<div className="row padding-top">
					<QueryBar getDocument={this.getDocument}/>
				</div>
				<BodyInput
					doc={this.state}
					onUpdateDocument={this.onUpdateDocument}
					onBodyChange={this.onBodyChange} />
			</div>
		)
	}
}