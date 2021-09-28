import json

js=json.load('sample.json')
dic=dict()
for chapter in js['chapters']:
  chapter_title=chapter['title']
  for lesson in chapter['lessons']:
    lesson_title=lesson['title']
    lesson_source=lesson['source']
