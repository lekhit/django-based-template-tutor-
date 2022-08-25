from hello.models import *
import re, json

pat = re.compile(r'\d{1,}')


def num(item, default=0):
    rs = pat.search(item)
    if rs:
        return float(rs[0])
    else:
        print(item, 'no index found so returned 0')
        return default


class update:
    def update_one(self, item, i):
        s = Source.objects.create(
            voe=item['source'],
            lesson=Lesson.objects.get_or_create(
                title=item.get("title"),
                course=Course.objects.get_or_create(
                    title=item.get("course"))[0],
                index=num(item.get('title'), i),
                chapter=Chapter.objects.get_or_create(
                    title=item.get('chapter'),
                    index=num(item.get('chapter'), i),
                    course=Course.objects.get_or_create(
                        title=item.get("course"))[0])[0])[0])

    def __init__(self, address=None):
        if address:
            self.put_data(address)

    def put_data(self, address):
        with open(address, 'r') as f:
            i = 0
            for item in json.load(f)['data']:
                i += 1
                self.update_one(item, i)



def Putdata(address):
    a = update()
    return a.put_data(address)
