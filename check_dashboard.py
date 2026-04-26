import urllib.request, urllib.parse, json
import re
from http.cookiejar import CookieJar

cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

login_url = 'http://127.0.0.1:8000/'
req1 = urllib.request.Request(login_url)
res1 = opener.open(req1)
html = res1.read().decode('utf-8')

match = re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"', html)
if match:
    csrf = match.group(1)
else:
    print("FAIL: CSRF not found")
    exit(1)

data = urllib.parse.urlencode({'csrfmiddlewaretoken': csrf, 'username': 'manager1', 'password': 'manager123'}).encode('utf-8')
req2 = urllib.request.Request(login_url, data=data)
res2 = opener.open(req2)

req3 = urllib.request.Request('http://127.0.0.1:8000/manager-dashboard/?date=2026-03-11')
res3 = opener.open(req3)
dashboard_html = res3.read().decode('utf-8')

print('SUCCESS' if 'Attendance is not marked' in dashboard_html and 'Python Programming' in dashboard_html else 'FAIL')
if 'SUCCESS' not in dashboard_html:
    print(dashboard_html[:1500])
