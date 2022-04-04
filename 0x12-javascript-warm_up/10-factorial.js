#!/usr/bin/node
const number = parseInt(process.argv[2]);

/**
 * getFactorial - function that get a factorial
 * @param (number) n - the number from which factoria if found
 * @return (number) - factorial of the number. -1 otherwise
 */
function getFactorial (n) {
  if (n < 0) return -1;
  if (isNaN(n) || n === 0) return 1;

  return n * getFactorial(n - 1);
}

console.log(getFactorial(number));
