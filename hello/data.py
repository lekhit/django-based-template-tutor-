import os
import requests
import json

class harper:
  url = "https://hdb01-patil1001970h01.harperdbcloud.com"

  def __init__(self):
      my_secret = os.environ['key']
      self.headers = {
  'Content-Type': 'application/json',
  'Authorization': my_secret
    }
  def courses(self):
    payload = json.dumps({
  "operation": "sql",
  "sql":f'select distinct(course_id) as id,course  from website.data;'
      })
    response = requests.request("POST", self.url, headers=self.headers, data=payload)
    return (json.loads(response.text))
  def lessons(self,course_id):
    payload = json.dumps({
  "operation": "sql",
  "sql":f'select   from website.data where course_id={course_id};'
      })
    response = requests.request("POST", self.url, headers=self.headers, data=payload)
    return (json.loads(response.text))








