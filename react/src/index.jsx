import React, { Component } from 'react'
import { render } from 'react-dom'
import { Router, Route, IndexRoute, browserHistory } from 'react-router'

import App from './App'

render(
  <App />,
  document.getElementById('reactApp')
)
