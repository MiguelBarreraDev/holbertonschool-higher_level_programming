#!/usr/bin/node
const numbers = process.argv.splice(2, 2).map(e => parseInt(e));

function add (a, b) {
  console.log(a + b);
}

add(...numbers);
