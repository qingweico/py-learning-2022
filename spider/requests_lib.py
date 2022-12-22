import requests

# pip install requests
print('------------- get -------------')
get_url = 'http://httpbin.org/get'
params = {'k': 'v'}
resp = requests.get(get_url, params)
print(resp.text)
print('------------- post -------------')
post_url = 'http://httpbin.org/post'
data = {'k': 'v'}
resp = requests.post(post_url, data)
print(resp.json())
