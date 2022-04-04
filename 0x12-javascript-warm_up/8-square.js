#!/usr/bin/node
const sizeOfSquare = parseInt(process.argv[2]);
const square = [];

if (isNaN(sizeOfSquare)) console.log('Missing size');
else {
  for (let i = 0; i < sizeOfSquare; i++) square.push('X');
  square.forEach(() => console.log(square.join('')));
}
