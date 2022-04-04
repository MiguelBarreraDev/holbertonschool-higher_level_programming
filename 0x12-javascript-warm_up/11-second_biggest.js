#!/usr/bin/node
const listOfNumbers = process.argv.splice(2).map((e) => parseInt(e)).sort((a,b) => b - a);
if (listOfNumbers.length <= 1) console.log(0);
else console.log(listOfNumbers[1]);
