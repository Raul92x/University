var assert      = require('assert');
var querystring = require('querystring');
var http        = require('http');

exports.getMessage = function(cb) {
  var options = {
      hostname: 'web0.ias.csusb.edu',
      auth: 'admin:cse405winter2014',
      port: 5984,
      path: '/read/message',
      method: 'GET'
  };
  send(options, function(err, data) {
    if (err) {
      console.log(err.message);
      return cb(err);
    }
    if (data.text === undefined) {
      throw new Error(
        'text property missing from msg document.\n' + JSON.stringify(data)
      );
    }
    cb(null, data.text);
  });
};

// Send request and receive data (a Javascript object).
// The options argument is the same as for http.request.
// cb = function(err, data)
function send(options, cb) {
  var req;

  // create request
  req = http.request(options, function(res) {
    var dataString;  // to be converted to Javascript object

    // tell node how to convert received bytes to a Javascript string
    res.setEncoding('utf8');

    // accumulate data
    res.on('data', function (chunk) {
      if (dataString === undefined) dataString = chunk; else dataString += chunk;
    });

    // parse received data
    res.on('end', function() {
      var data;
      try {
        data = JSON.parse(dataString);
      } catch (err) {
        return cb(err);
      }
      cb(null, data);
    });
  });

  // register error listener
  // pass error directly to callback
  req.on('error', cb);

  // send request
  req.end();
};
