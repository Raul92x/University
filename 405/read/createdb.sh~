echo Delete the test database.
curl -X DELETE http://admin:cse405winter2014@web0.ias.csusb.edu:5984/read

echo Create the test database.
curl -X PUT http://admin:cse405winter2014@web0.ias.csusb.edu:5984/read

echo Insert the security object.
curl -X PUT http://admin:cse405winter2014@web0.ias.csusb.edu:5984/read/_security  \
     -H "Content-type: application/json"                     \
     -d "{\"members\":{\"names\":[\"admin\"]}}"

echo Insert docs.
curl -X POST http://admin:cse405winter2014@web0.ias.csusb.edu:5984/read  \
     -H "Content-type: application/json"                     \
     -d "{\"_id\":\"message\",\"text\":\"the read assignment\"}"
