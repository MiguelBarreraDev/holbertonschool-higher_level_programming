#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];

fs.promises.readFile(fileName, 'utf8')
  .then(res => console.log(res))
  .catch(err => console.log(err));
