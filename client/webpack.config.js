var babelPresets = {presets: ['react', 'es2015']};
var path = require('path');
var webpack = require('webpack');

module.exports = {
	devtool: 'eval',
	entry: [
		"webpack-dev-server/client?http://localhost:8080/",
		"webpack/hot/only-dev-server",
		"./src/index.js"
	],
	output: {
		path: path.join(__dirname, 'dist'),
		filename: "bundle.js",
		publicPath: '/static/'
	},
	module: {
		loaders: [
			{
				test: /\.js$/,
				include: path.join(__dirname, 'src'),
				loaders: ['react-hot', 'babel'],
			}
		]
	}
};