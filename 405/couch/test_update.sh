echo Update document a.
curl -X PUT http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test/a                        \
     -H "Content-type: application/json"                                   \
     -d "{\"_id\":\"a\",\"x\":100,\"_rev\":\"1-0785e9eb543380151003dc452c3a001a\"}"
echo
echo Display document a.
curl -X GET http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test/a
echo
echo Try an update with an old revision number.  Note a conflict.
curl -X PUT http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test/a                        \
     -H "Content-type: application/json"                                   \
     -d "{\"_id\":\"a\",\"x\":999,\"_rev\":\"1-0785e9eb543380151003dc452c3a001a\"}"
echo
echo Display document a.  Note that x is still 100.
curl -X GET http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test/a
