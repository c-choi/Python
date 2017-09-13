import requests
from requests_oauthlib import OAuth1

consumer_key = 'WEC1zoPawQPZg0Jfq7YFzauhb'
consumer_secret = 'y99rG3xim0ybjfOvlDSyFM8MNHC8GuuxpsQJCY7q0DS5tICVVe'
access_token = '347001906-d8eoJzRnRN7pNIQb1TzY6wLORCzWdNXy1mwgKVZU'
access_token_secret = 'Zra3ZnWFDJViVuvJvjFZVLvtw1uVIuLUuS9Us4JseK9V0'

oauth = OAuth1(client_key=consumer_key, client_secret=consumer_secret, resource_owner_key=access_token, resource_owner_secret=access_token_secret)

url = 'https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name={0}'.format('ccloudyc')
# screen name 이 naver_d2인 정보의 타임라인 정보를 가져와라
r = requests.get(url=url, auth=oauth)
statuses = r.json()
print(statuses)
# for status in statuses:
#     print(status['text'], status['created_at'])