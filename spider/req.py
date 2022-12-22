from urllib import request

url = 'http://106.12.136.221'
resp = request.urlopen(url, timeout=1)
print(resp.read().decode('utf-8'))
