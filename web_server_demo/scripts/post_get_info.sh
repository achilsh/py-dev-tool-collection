#! /usr/bin/env bash 
curl -X POST http://127.0.0.1:8080/demo/v1/user/call/get_info \
  -H "Content-Type: application/json" \
  -d @- <<EOF | jq
{
    "id": 1,
    "username": "achilsh",
    "email": "hwshtongxin@126.com"
}
EOF
