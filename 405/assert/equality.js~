var assert = require('assert').ok;

var a = 0;
var b = 0;
var c = { x: '0' };
var d = { x: '0' };
var e = c;

// compare 0 and false
assert(0 == false);
assert(0 !== false);

// compare 1 and true
assert(1 == true);
assert(1 !== true);

//compare 3 and true
assert(3 != true);
assert(3 !== true);

// compare 0 and null
assert(0 != null);
assert(0 !== null);

// compare 0 and undefined
assert(0 != undefined);
assert(0 !== undefined);

// compare 0 and ""
assert(0 == "");
assert(0 !== "");

// compare 0 and '0'
assert(0 == '0');
assert(0 !== '0');

// compare 0 and 'false'
assert(0 != 'false');
assert(0 !== 'false');

// compare 3 and '3'
assert(3 == '3');
assert(3 !== '3');

// compare true and 'true'
assert(true != 'true');
assert(true !== 'true');

// compare false and 'false'
assert(0 != null);
assert(0 !== null);

// compare null and false
assert(null != false);
assert(null !== false);

// compare null and undefined
assert(null == undefined);
assert(null !== undefined);

// compare null and 0
assert(null != 0);
assert(null !== 0);

// compare undefined and global.x1234
assert(undefined == global.x1234);
assert(undefined === global.x1234);

// compare { x:0 } and { x:0 }
assert({ x:0 } != { x:0 });
assert({ x:0 } !== { x:0 });

// compare 'a' and 'a'
assert('a' == 'a');
assert('a' === 'a');

// compare a where var a = 0  and  b where var b = 0
assert(a == b );
assert(a === b );

// compare c where var c = { x: 0 }  and  d where var d = { x: 0 }
assert(c != d );
assert(c !== d );

// compare c where var c = { x: 0 }  and  e where var e = c
assert(c == e );
assert(c === e );

console.log("All tests passed.");





















