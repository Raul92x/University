var extractData           = require('./request').extractData;
var checkStringParameters = require('./request').checkStringParameters;
var checkPassword         = require('./request').checkPassword;
var checkRevision         = require('./request').checkRevision;
var reply                 = require('./response').reply;
var replyError            = require('./response').replyError;
var replyNonUser          = require('./response').replyNonUser;
var replyNotAllowed       = require('./response').replyNotAllowed;
var db                    = require('./db');
var updateDoc             = require('./db').updateDoc;

exports.handle = function(req, res) {
  // Pass request through appropriate filters before performing end goal processing.
  extractData(req, 256, function(data) {
    //console.log(JSON.stringify(data));
    checkStringParameters(data, ['_id', '_rev', 'pw', 'id'], req, function() {
      checkPassword(data._id, data.pw, res, function(userDoc) {
        checkRevision(userDoc, data._rev, res, function() {
          processRequest(userDoc, data.id, data._id, res);
        });
      });
    });
  });
};

function processRequest(userDoc, id, _id, res) {
  if (userDoc.gems <= 0) {
    return reply(res, { 'insufficientGems': true });
  }

  if (id === _id) {
    replyNotAllowed(res);
  } else {
    db.getDoc(id, function(err, bdoc) {
      if (err) {
        console.log(err.message);
        replyError(res);
      } else if (bdoc === null) {
        replyNonUser(res);
      } else {
        processRequest2(userDoc, bdoc, res);
      }
    });
  }
};

function processRequest2(userDoc, bdoc, res) {

  --userDoc.gems;
  ++bdoc.gems;

  updateDoc(bdoc, function(err, result) {
    if (err) {
      console.log(err.message);
      replyError(res);
    } else if (result.old) {
      processOld(bdoc, res);
    } else if (result.rev) {
      bdoc._rev = result.rev;
      processRequest3(userDoc, res);
    } else {
      console.log('logic error');
      replyError(res);
    }
  });
};

function processRequest3(userDoc, res) {

  updateDoc(userDoc, function(err, result) {
    if (err) {
      console.log(err.message);
      replyError(res);
    } else if (result.old) {
      processOld(userDoc, res);
    } else if (result.rev) {
      userDoc._rev = result.rev;
      reply(res, { doc: userDoc });
    } else {
      console.log('logic error');
      replyError(res);
    }
  });
};

function processOld(oldDoc, res) {
  // Get a fresh version of the doc and return it to the client.
  checkPassword(oldDoc._id, oldDoc.pw, res, function(newDoc) {
    reply(res, { old: true, doc: newDoc });
  });
}
