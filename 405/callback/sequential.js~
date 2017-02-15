function f(cb) 
{
  console.log("f's activity starts.");
  var t = Math.random() * 5000; //gives a num between 0 and 1000

  function onActivityDone()
  {
    console.log("f's activity ends.");
    if (cb) cb();
  }

  setTimeout(onActivityDone, t);
}

f(function()
{
  f(function()
  {
    f(function()
    {
      console.log('Done.');
    });
  });
});
