import React from 'react';
import ReactDOM from 'react-dom';
import App from './components/App';

console.log("Loading React app...");

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);