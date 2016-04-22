import React, { Component } from 'react';

export default class BodyInput extends Component {
	constructor(props) {
		super(props);
		this.state = {title: props.doc.title, body: props.doc.body || ""}
	}

	render() {
		let props = this.props;
		return (
			<div>
				<div className="row padding-top">
					<div className="col-xs-12">

						<textarea
							className="form-control"
							rows="20"
							value={props.doc.body}
							onChange={(e) => props.onBodyChange(e.target.value)}>
						</textarea>

					</div>
				</div>
				<div className="row padding-top">
					<div className="col-xs-12">
						<button
							className="btn btn-success btn-block"
							onClick={() => { props.onUpdateDocument() }}>Update
						</button>
					</div>
				</div>
			</div>
		)
	}
}

export default BodyInput;