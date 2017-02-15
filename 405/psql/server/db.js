var pg = require('pg');

var url = 'postgres://localhost/gift'; // or 'postgres://postgres@localhost/gift'

exports.init = function(cb) {
  pg.connect(url, function(err, client, done) {
    if (err) throw err;
    client.query("select * from users where _id = 'a'", function (err, result) {
      done();
      if (err) throw err;
      cb();
    })
  });
};

exports.getDoc = function(_id, cb) {
  pg.connect(url, function(err, client, done) {
    if (err) return cb(err);
    client.query('select * from users where _id = $1', [_id], function (err, result) {
      done();
      if (err) return cb(err);
      if (result.rows.length === 0) {
        return cb(null, null);
      }
      cb(null, result.rows[0]);
    });
  });
};

exports.updateDoc = function(doc, cb) {
  pg.connect(url, function(err, client, done) {
    if (err) return cb(err);
    var nextRev = (parseInt(doc._rev) + 1).toString();
    client.query("update users set balance = $1, gems = $2, score = $3, _rev = $4 where _id = $5 and _rev = $6",
                 [doc.balance, doc.gems, doc.score, nextRev, doc._id, doc._rev],
                 function (err, result) {
      done();
      if (err) {
        cb(err);
      } else if (result.rowCount === 0) {
        // Assume the doc is there. If it's not, I think the code still works fine.
        cb(null, { old: true });
      } else {
        cb(null, { rev: nextRev });
      }
    });
  });
};

