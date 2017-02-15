var assert = require('assert').ok;

var obj = (function() {
		   var x = 3;
		   return {
		   getX: function() { return x; },
		   setX: function(value) { x = value; },
		   getNegativeX: function() { return -x; }
		   };
		   })();

assert(typeof(x) === 'undefined');
assert(obj.getX() === 3);
assert(obj.getNegativeX() === -3);

obj.setX(4);
assert(obj.getX() === 4);

console.log("All tests passed.");
