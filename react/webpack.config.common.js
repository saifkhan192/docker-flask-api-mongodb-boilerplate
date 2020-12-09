const webpack = require('webpack');
const path = require('path');
const merge = require('webpack-merge');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const webpackCommonConfig = {
	context: __dirname,
	entry: './src/index.jsx',
	output: {
		path: '/app/web-dist', // absolute output path for bundle
		filename: 'bundle.js',
	},
	resolve: {
		extensions: ['.js', '.jsx'],
	},
	module: {
		rules: [
			{
				test: /\.(js|jsx)$/,
				loader: 'babel-loader',
				exclude: /node_modules/
			},
			{
				test: /\.(sa|sc|c)ss$/,
				use: [
				  {
					loader: MiniCssExtractPlugin.loader,
					options: {
					  hmr: process.env.NODE_ENV === 'development',
					},
				  },
				  'css-loader',
				  'sass-loader',
				],
			},
		]
	},
	plugins: [
		new MiniCssExtractPlugin({
			filename: 'bundle.css',
		}),
	],
	watchOptions: {
		ignored: [
			'node_modules/**', 
		]
	}
}

module.exports = webpackCommonConfig;
