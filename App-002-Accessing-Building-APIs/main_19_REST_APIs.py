import requests

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-11-01&to=2023-11-02&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')
content = r.json()
print(type(content))
print(content['articles'][0]['description'])
