from requests import get

endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:3000/api/"

get_response = get(url=endpoint,
                   params={"abc": 123},
                   json={"query": "Hello World"})

# print(get_response.text)
print(get_response.json())
print(get_response.status_code)
