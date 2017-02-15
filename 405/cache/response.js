var http = require('http');

var body;
var etag;

exports.generateETag = function(buffer){
  var shasum = require('crypto').createHash('sha1');
  shasum.update(buffer, 'binary');
  return shasum.digest('hex');
};



exports.replyNotModified = function(res) {
  res.writeHead(304);
  res.end();
};
