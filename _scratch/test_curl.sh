#!/bin/bash
TOKEN=$(jq -r '.activeId as $id | .companies[] | select(.companyId == $id) | .token' config.json)
if [ -z "$TOKEN" ]; then
    TOKEN=$(jq -r '.token' config.json)
fi
CID=$(jq -r '.activeId' config.json)
if [ -z "$CID" ]; then
    CID=$(jq -r '.companyId' config.json)
fi

curl -v -X POST "https://bi-engine.sesametime.com/api/v3/analytics/report-query" \
  -H "Authorization: Bearer $TOKEN" \
  -H "x-company-id: $CID" \
  -H "csid: $CID" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
  -H "Origin: https://app.sesametime.com" \
  -H "Referer: https://app.sesametime.com/" \
  -d '{"moduleName": "work-entries", "limit": 50, "columns": ["id"]}'
