module.exports = {
	entry: [
		"webpack-dev-server/client?http://localhost:8080/public",
		"webpack/hot/only-dev-server",
		"./app/components/Main.js"
	],
	output: {
		filename: "public/bundle.js"
	},
	module: {
		loaders: [
			{
				test: /\.jsx?$/,
				exclude: /(node_modules|bower_components)/,
				loaders: ['react-hot', 'babel-loader'],
			}
		]
	}
};