function f(cb) 
{
  console.log("f's activity starts.");
  var t = Math.random() * 5000; //gives a num between 0 and 5000

  function onActivityDone()
  {
    console.log("f's activity ends.");
    if (cb) cb();
  }
  setTimeout(onActivityDone, t);
}

var completions = 0;
function done()
{
  ++completions;
  if (completions === 3)
  {
    console.log('Done.');
  }
}

f(done);
f(done);
f(done);
