const webpack = require('webpack');
const merge = require('webpack-merge');
const webpackCommonConfig = require('./webpack.config.common');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = merge(webpackCommonConfig, {
	mode: 'production',
    optimization: {
        minimizer: [
            new UglifyJsPlugin({
                uglifyOptions: {
                    mangle: true,
                    warnings: false,
                    compress: {
                        pure_getters: true,
                        unsafe: true,
                        unsafe_comps: true,
                    },
                    output: {
                        comments: false,
                    },
                },
                exclude: [/\.min\.js$/gi] // skip pre-minified libs
            }),
        ],
    },
	plugins: [
		new webpack.EnvironmentPlugin({ NODE_ENV: 'production' }),
	]
});
