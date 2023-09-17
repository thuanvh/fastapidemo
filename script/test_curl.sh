#API_URL=https://c4z96jmop3.execute-api.us-east-1.amazonaws.com
API_URL=http://127.0.0.1:8000/api
echo "'$API_URL"/books"'"

curl -X 'POST' \
  "$API_URL/books" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "/books/id1",
  "author": "/authors/id1",
  "name": "Hello world",
  "note": "Good book",
  "serial": "alk12314"
}'


curl -X 'GET' \
   "$API_URL/books/id1" \
   -H 'accept: application/json'
