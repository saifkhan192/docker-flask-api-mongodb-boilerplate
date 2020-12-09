const webpack = require('webpack');
const merge = require('webpack-merge');
const webpackCommonConfig = require('./webpack.config.common');

module.exports = merge(webpackCommonConfig, {
	mode: 'development',
	devtool: "source-map",
	plugins: [
		new webpack.EnvironmentPlugin({ NODE_ENV: 'development' }),
	]
});