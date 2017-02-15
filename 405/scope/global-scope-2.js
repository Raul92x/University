var x = 3;
console.log(global.x);  // undefined
global.x = x;
console.log(global.x); // 3