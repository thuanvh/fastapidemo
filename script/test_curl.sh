curl -X 'POST' \
  'https://c4z96jmop3.execute-api.us-east-1.amazonaws.com/books' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": -1,
  "author": 0,
  "name": "",
  "note": "string",
  "serial": ""
}'

curl -X 'GET' \
  'https://c4z96jmop3.execute-api.us-east-1.amazonaws.com/books/1' \
  -H 'accept: application/json'