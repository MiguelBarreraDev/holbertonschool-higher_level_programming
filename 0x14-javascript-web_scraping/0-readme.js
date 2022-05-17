#!/usr/bin/node
const fs = require('fs');
const fileName = process.argv[2];

fs.readFile(fileName, 'utf8', (err, res) => {
  if (err) console.log(err);
  else console.log(res);
});
