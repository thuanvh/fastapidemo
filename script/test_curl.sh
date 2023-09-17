#API_URL=https://72nwcbb2b6.execute-api.ap-southeast-1.amazonaws.com
API_URL=http://127.0.0.1:8000/api
echo "'$API_URL"/books"'"

curl -X 'POST' \
  "$API_URL/books" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "/books/id1",
  "author": "/authors/id1",
  "name": "Hello World",
  "note": "Good book",
  "serial": "alk12314123"
}'


curl -X 'GET' \
   "$API_URL/books/id1" \
   -H 'accept: application/json'
