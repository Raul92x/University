var assert = require('assert').ok;

function getGetXFunction()
{
	var x = 3;
	function getX() { return x; }
	return getX;
}

assert(typeof(x) === 'undefined');

var getX = getGetXFunction();
assert(getX() === 3);

console.log("All tests passed.");
