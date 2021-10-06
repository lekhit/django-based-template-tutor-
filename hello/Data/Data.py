import requests
import json,re
pat=re.compile(r"(\d+){1,}")

'''

url = "https://hdb01-patil1001970h01.harperdbcloud.com"

payload = json.dumps({
  "operation": "create_table",
  "schema": "dev",
  "table": "breed",
  "hash_attribute": "id"
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic cGF0aWw6ZHIxMDAxOTcw'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
'''