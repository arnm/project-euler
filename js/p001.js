/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

var mr = require('mori');

function solve() {
  var multiples = mr.filter(function (n) {
    return n % 3 === 0 || n % 5 === 0;
  }, mr.range(1000));
  var answer = mr.reduce(mr.sum, multiples);
  return answer;
}

console.log('Answer:', solve());
