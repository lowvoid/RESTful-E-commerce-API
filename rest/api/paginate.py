import requests

page = 1
has_next_page = True

while has_next_page:
    endpoint = "http://localhost:8000/products/"
    params = {'page': page}
    data = requests.get(endpoint, params=params).json()
    print(data.get('next'))
    has_next_page = data.get('next') is not None
    page += 1
