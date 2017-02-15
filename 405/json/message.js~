var http = require('http');

var responseObject = { msg: 'Hello JSON.' };
var responseString = JSON.stringify(responseObject);
var body = new Buffer(responseString, 'utf-8');

exports.handle = function(req, res) {
  res.writeHead(200, {
    'Content-Type': 'application/json',
    'Content-Length': body.length
  });
  res.end(body);
};
