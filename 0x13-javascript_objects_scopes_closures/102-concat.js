#!/usr/bin/node
const fs = require('fs');
const [target, ...sourceFiles] = process.argv.splice(2).reverse();

function readToWrite (listOfSourceFiles = Array, target = String) {
  try {
    let data = '';
    for (const pathFile of listOfSourceFiles.reverse()) {
      data += fs.readFileSync(pathFile, 'utf8');
    }
    fs.writeFileSync(target, data);
  } catch (err) {
    console.error(err);
  }
}

readToWrite(sourceFiles, target);
