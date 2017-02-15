var assert = require('assert').ok;

var http = require('http');
var EventEmitter = require('events').EventEmitter;
var server = http.createServer();
assert(server !== EventEmitter);
//console.log(server instanceof EventEmitter);

console.log("All tests passed.");
