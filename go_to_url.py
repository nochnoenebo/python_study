import http.client
import mimetypes
conn = http.client.HTTPSConnection("api.todoist.com")
payload = ''
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer 5f90a9e104608718f09c637be561e143799fd3bd'
}
conn.request("GET", "/rest/v1/tasks", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))