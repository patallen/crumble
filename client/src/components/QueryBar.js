import React, { Component } from 'react';


export default class QueryBar extends Component {
	constructor(props) {
		super(props);
		this.state = {query: ""};
	}
	handleClick(event) {
		let query = this.state.query;
		this.props.getDocument(query);
	}
	render() {
		return (
			<div>
				<div className="col-xs-10">
					<input
						className="form-control"
						value={this.state.query}
						onChange={e => this.setState({query: e.target.value})}
					/>
				</div>
				<div className="col-xs-2">
					<button
						className="btn btn-success btn-block"
						onClick={this.handleClick.bind(this)}>
							Go!
					</button>
				</div>
			</div>
		)
	}
}