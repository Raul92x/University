var assert = require('assert').ok;

var mod3 = require('./mod3');
assert(mod3.x === 3);

mod3.x = 10;
assert(mod3.getX() === 10);

console.log("All tests passed.");
