var assert = require('assert').ok;

function divideby(x, y, cb)
{

  if (y == 0)
  {
    cb(new Error('Division by zero is undefined.'));
  }
  else
  {
  
  }
}
    // If y is zero, return an instance or Error in the first argument of cb.
    // Otherwise, divide x by y and return the result in the second argument of cb
    // and set the first argument to null to indicate no error.





divideby(6, 3, function(err, result)
{
    // Assert that err is null.
    assert(err === null);
    // Assert that result is 2.
    assert(result == 2);
});

divideby(6, 0, function(err, result) 
{
    // Assert that err is not null.
    assert(err !== null);

    // Assert that result is undefined.
    assert(result === undefined);
    // Assert that type of err.message is a string.
    //assert(......);
});

console.log('All tests passed');

