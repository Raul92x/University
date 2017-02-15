var assert = require('assert').ok;

var getX = (function() {
  var x = 3;
  return function() { return x; }
})();

assert(typeof(x) === 'undefined');
assert(getX() === 3);

console.log("All tests passed.");
