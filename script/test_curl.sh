#API_URL=https://c4z96jmop3.execute-api.us-east-1.amazonaws.com
API_URL=http://127.0.0.1:8000
echo "'$API_URL"/books"'"

# curl -X 'POST' \
#   "'$API_URL"/books' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "id": -1,
#   "author": 0,
#   "name": "",
#   "note": "string",
#   "serial": ""
# }'


# curl -X 'GET' \
#   '"'$API_URL"/books/1"'"' \
#   -H 'accept: application/json'

curl -X 'GET' \
  'http://127.0.0.1:8000/books/id1' -H 'accept: application/json'