var assert = require('assert');

function imgood() {
  if (2 + 2 !== 4) {
    throw new Error('Something\'s wrong.');
  }
}

function imbad() {
    throw new Error('I\'m bad.');
}

imgood();
assert.throws(imbad);
console.log('All tests passed.');
