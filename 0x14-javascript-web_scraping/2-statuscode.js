#!/usr/bin/node
const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(res => console.log('code:', res.status))
  .catch(err => {
    if (err.response) console.log('code:', err.response.status);
    else console.log(err.message);
  });
