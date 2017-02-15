var http = require('http');
var getMessage = require('./db').getMessage;


exports.handle = function(req, res) {
  getMessage(function(err, message) {
    if (err) {
      console.log(err.message);
      res.writeHead(500, 'server error');
      res.end();
      return;
    }
    var responseObject = { msg: message };
    var responseString = JSON.stringify(responseObject);
    var body = new Buffer(responseString, 'utf-8');

    res.writeHead(200, {
      'Content-Type': 'application/json',
      'Content-Length': body.length,
      'Pragma': 'no-cache',
      'Cache-Control': 'no-cache, no-store'
    });
    res.end(body);
  });
};
