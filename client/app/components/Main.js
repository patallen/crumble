import React from 'react';
import ReactDOM from 'react-dom';

class Main extends React.Component {
	render() {
		return <h1>Hello, It's me.</h1>
	}
}

var app = document.getElementById('app');
ReactDOM.render(<Main />, app);