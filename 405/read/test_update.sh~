echo Update document with id 'message'.
echo Try an update with an old revision number.  Note a conflict.
curl -X PUT http://admin:cse405winter2014@web0.ias.csusb.edu:5984/read/message                    \
     -H "Content-type: application/json"                                                           \
     -d "{\"_id\":\"message\",\"text\":\"the new message\",\"_rev\":\"1-46efe3000869300c3df0006158abebed\"}"

