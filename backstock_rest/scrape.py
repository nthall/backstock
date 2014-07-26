import json
import os
import requests
import sys
from bs4 import BeautifulSoup

sys.path.append('/usr/src/backstock')
os.environ['DJANGO_SETTINGS_MODULE'] = 'backstock.settings'
from backstock_rest.models import Photo

# their json response is actually jsonp i guess?
def extract_obj(text):
  start = text.find('{')
  end = text[::-1].find('}') * -1
  return (json.loads(text[start:end]))


# takes a list of posts and puts them in the db
def insert(posts):
  for post in posts:
    tumblr_id = post['id']
    if (Photo.objects.filter(tumblr_id=tumblr_id)):
      continue
    tumblr_url = post['url-with-slug']
    if 'tags' in post:
      tags = ', '.join(post['tags'])
    else:
      tags = ''
    src = post['photo-url-1280']

    p = Photo(tumblr_id=tumblr_id, tumblr_url=tumblr_url, src=src, tags=tags)
    p.save()


# just scrape all existing posts to start. (invoke from interpreter)
def bootstrap(get=0):
  url = "http://nos.twnsnd.co/api/read/json"
  data = {'num': 50, 'start': get}
  r = extract_obj(requests.get(url, params=data).text)
  insert(r['posts'])
  
  if len(Photo.objects.all()) < r['posts-total']:
    bootstrap(get+50)

# assume nightly cron, assume they don't add a boatload any given day
def main():
  url = "http://nos.twnsnd.co/api/read/json"
  r = extract_obj(requests.get(url))
  insert(r['posts'])


if __name__ == '__main__':
  main()
