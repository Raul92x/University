var http = require('http');

var body;

exports.handle = function(req, res) {
  res.writeHead(200, {
    'Content-Type': 'image/png',
    'Content-Length': body.length
  });
  res.end(body);
};

exports.init = function(cb) {
  require('fs').readFile('image.png', function(err, data) {
    if (err) throw err;
    body = data;
    cb();
  });
}