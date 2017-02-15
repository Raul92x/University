var assert = require('assert').ok;

var x = 1;
var y = 2;

assert(x === 1);
assert(y === 2);

function test()
{
   x = 10;
   y = 20;
   var y;
}

test();

assert(x === 10);
assert(y === 2);

console.log("All tests passed.");
