import React, { Component } from 'react';


export default class QueryBar extends Component {
	constructor(props) {
		super(props);
		this.state = {query: ""};
	}
	handleQueryChange(event) {
		this.setState({query: event.target.value})
	}
	handleBtnClick() {
		console.log("btn was clicked")
	}
	render() {
		return (
			<div>
				<div className="col-xs-10">
					<input
						className="form-control"
						value={this.state.query}
						onChange={this.handleQueryChange.bind(this)}
					/>
				</div>
				<div className="col-xs-2">
					<button className="btn btn-success btn-block" onClick={this.handleBtnClick.bind(this)}>Go!</button>
				</div>
			</div>
		)
	}
}