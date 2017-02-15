var http = require('http');
var domain = require('domain');
var root = require('./root');
var image = require('./image');
var message = require('./message');

function replyError(res) {
  try {
    res.writeHead(500);
    res.end('Server error.');
  } catch (err) {
    console.error('Error sending response with code 500.');
  }
};

function replyNotFound(res) {
  res.writeHead(404);
  res.end('not found');
}

function handleRequest(req, res)
{
  console.log('Handling request for ' + req.url);
  if (req.url === '/') 
  {
    root.handle(req, res);
  }
  else if (req.url === '/image.png') 
  {
    image.handle(req, res);
  } 
  else if (req.url.substr(0, 8) === '/message') 
  {
    message.handle(req, res);
  } 
  else
  {
    replyNotFound(res);
  }
}

var server = http.createServer();

server.on('request', function(req, res) {
  var d = domain.create();
  d.on('error', function(err) {
    console.error(req.url, err.message);
    replyError(res);
  });
  d.run(function() { handleRequest(req, res); });
});


var n = 1;
function done() 
{
  if (--n === 0) server.listen(5000);
}

root.init(done);
image.init(done);
