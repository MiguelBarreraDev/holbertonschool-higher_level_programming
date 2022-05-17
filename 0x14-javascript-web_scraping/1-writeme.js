#!/usr/bin/node
const fs = require('fs');
const [filePath, text] = process.argv.slice(2);

try {
  fs.writeFileSync(filePath, text, { encoding: 'utf-8' });
} catch (err) {
  console.log(err);
}
