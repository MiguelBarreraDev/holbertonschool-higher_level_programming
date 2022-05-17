#!/usr/bin/node
const axios = require('axios').default;
const fs = require('fs');
const [url, filePath] = process.argv[2].slice(2);

axios.get(url)
  .then(({ data }) => {
    fs.writeFile(filePath, data, 'utf-8', err => console.log(err));
  })
  .catch(err => console.log(err));
