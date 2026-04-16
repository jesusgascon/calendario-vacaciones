import urllib.request, json
with open("config.json") as f: config = json.load(f)
token = config.get("token")
cid = config.get("activeId") or config.get("companyId")
cookies = "KnownUser=true; _gcl_au=1.1.1430557543.1774250719; _ga=GA1.1.102386141.1774250714; hubspotutk=98733fe58c9f33e054f44e6f5596bd20; _fbp=fb.1.1774250719180.722447521547719215; _tt_enable_cookie=1; _ttp=01KMCSAY1457WNHPZCNHB99G7W_.tt.1; AMP_MKTG_7c60114df6=JTdCJTdE; _clck=1qch3fn%5E2%5Eg59%5E1%5E2273; __hstc=151978342.98733fe58c9f33e054f44e6f5596bd20.1774250718936.1776275470154.1776327574398.39; __hssrc=1; __hssc=151978342.3.1776327574398; _uetsid=82c0ccc0373811f1965bc9d75f0a2862; _uetvid=5b4555c0229e11f1ad4705ad9725bf9a; AMP_7c60114df6=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI3ZDFjMzc5OS0xMTYxLTQ4NWMtYjIxMy1lZjRmNzBmNWMwNTAlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJhYjFiMmE3ZS1iOTIxLTRlNWUtYjVkOC1kM2I1NGVhN2U1YTAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzc2MzI3NTc5MjkzJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc3NjMyODA4NzEwNiUyQyUyMmxhc3RFdmVudElkJTIyJTNBNDYyJTJDJTIycGFnZUNvdW50ZXIlMjIlM0EwJTJDJTIyY29va2llRG9tYWluJTIyJTNBJTIyLnNlc2FtZXRpbWUuY29tJTIyJTdE; _ga_ZGLSYVSQLT=GS2.1.s1776327579$o38$g1$t1776328087$j60$l0$h0; _clsk=1gz6ybb%5E1776328087703%5E14%5E1%5Ez.clarity.ms%2Fcollect; ttcsid=1776327574619::dJuLDQJLWnsoQD90IUt3.42.1776328149354.0::1.512416.145067::574728.36.445.207::0.0.0; ttcsid_D0RE6NBC77UA68QT2DT0=1776327574619::WVunqZjsBdSYjjXFuvjX.42.1776328149354.1; _ga_C1G7T2YG10=GS2.1.s1776327573$o41$g1$t1776328205$j60$l0$h0; _ga_4JNY26TSTY=GS2.1.s1776327573$o41$g1$t1776328205$j60$l0$h0"
headers = {
    "Authorization": f"Bearer {token}", "csid": cid, "x-company-id": cid,
    "Cookie": cookies, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Origin": "https://app.sesametime.com", "Referer": "https://app.sesametime.com/"
}
payload = b'{"from": "schedule_context_check","select": [{"field": "schedule_context_check.date", "alias": "date"}],"limit": 5}'
req = urllib.request.Request("https://bi-engine.sesametime.com/api/v3/analytics/report-query", headers=headers, data=payload, method="POST")
try:
    with urllib.request.urlopen(req) as r:
        print("OK!", r.status)
except Exception as e:
    print("FAILED", e.code, e.read().decode()) if hasattr(e, 'read') else print(e)
