/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we
get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/

var ld = require('lodash-node')

var multiples = ld.filter(ld.range(1000), function(n) { return n % 3 == 0 || n % 5 == 0 })
var answer = ld.reduce(multiples, function(x, y) { return x + y })

console.log('Answer:', answer)
