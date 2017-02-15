var http = require('http');

http.createServer(function (request, response) {
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Goodbye World\n');
}).listen(5000);

console.log('Server running at http://127.0.0.1:5000/');
