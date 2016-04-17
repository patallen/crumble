import React from 'react';

export default class Main extends React.Component {
	render() {
		return (
			<div className="main col-md-offset-3 col-md-6">
				<div className="row padding-top">
					<div className="col-xs-10">
						<input className="form-control" />
					</div>
					<div className="col-xs-2">
						<button className="btn btn-success btn-block">Go!</button>
					</div>
				</div>
				<div className="row padding-top">
					<div className="col-xs-12">
						<textarea className="form-control" rows="20"></textarea>
					</div>
				</div>
				<div className="row padding-top">
					<div className="col-xs-12">
						<button className="btn btn-success btn-block">Update</button>
					</div>
				</div>
			</div>
		)
	}
}