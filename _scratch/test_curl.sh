#!/bin/bash
source /home/jesus/.bashrc 2>/dev/null || true
token=$(jq -r '.token' config.json)
cid=$(jq -r '.companies[0].companyId' config.json)

curl "https://bi-engine.sesametime.com/api/v3/analytics/report-query" \
  -H "accept: application/json, text/plain, */*" \
  -H "accept-language: es-ES,es;q=0.9,en;q=0.8" \
  -H "authorization: Bearer $token" \
  -H "content-type: application/json" \
  -H "csid: $cid" \
  -H "origin: https://app.sesametime.com" \
  -H "referer: https://app.sesametime.com/" \
  -H "sec-ch-ua: \"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"" \
  -H "sec-ch-ua-mobile: ?0" \
  -H "sec-ch-ua-platform: \"Windows\"" \
  -H "sec-fetch-dest: empty" \
  -H "sec-fetch-mode: cors" \
  -H "sec-fetch-site: same-site" \
  -H "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36" \
  -H "x-company-id: $cid" \
  -H "x-region: EU1" \
  --data-raw '{"from":"schedule_context_check","select":[{"field":"schedule_context_check.date","alias":"date"}],"limit":5}' \
  --compressed -si
