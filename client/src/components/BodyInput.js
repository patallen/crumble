import React from 'react';

const BodyInput = ({ body, onUpdateDocument, onBodyChange }) => {
	return (
		<div>
			<div className="row padding-top">
				<div className="col-xs-12">
					<textarea className="form-control" rows="20" defaultValue={body} onChange={(e) => onBodyChange(e.target.value)}></textarea>
				</div>
			</div>
			<div className="row padding-top">
				<div className="col-xs-12">
					<button className="btn btn-success btn-block" onClick={() => { onUpdateDocument() }}>Update</button>
				</div>
			</div>
		</div>
	)
}

export default BodyInput;