echo Delete the test database.
curl -X DELETE http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test

echo Create the test database.
curl -X PUT http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test

echo Insert the security object.
curl -X PUT http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test/_security  \
     -H "Content-type: application/json"                     \
     -d "{\"members\":{\"names\":[\"admin\"]}}"

echo Insert docs.
curl -X POST http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test  \
     -H "Content-type: application/json"                     \
     -d "{\"_id\":\"a\",\"x\":1}"

echo Insert docs.
curl -X POST http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test  \
     -H "Content-type: application/json"                     \
     -d "{\"_id\":\"b\",\"x\":2}"

echo Insert docs.
curl -X POST http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test  \
     -H "Content-type: application/json"                     \
     -d "{\"_id\":\"c\",\"y\":1}"

echo Insert docs.
curl -X POST http://admin:cse405winter2014@web0.ias.csusb.edu:5984/test  \
     -H "Content-type: application/json"                     \
     -d @d.json
