import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users/'
USERNAME = 'USERNAME'
TOKEN = 'TOKEN'
graphID = 'GRAPH_ID'
today = datetime.today().strftime('%Y%m%d')

header = {
    'X-USER-TOKEN': TOKEN
}

"""
INITIAL SETUP
________________________________________________________________

user_params = {
    'username': USERNAME,
    'token': TOKEN,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


CREATE GRAPH
________________________________________________________________
graph_endpoint = f'{pixela_endpoint}{USERNAME}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'Coding in Python',
    'unit': 'hours',
    'type': 'int',
    'color': 'sora'
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
print(response.text)

"""

# Send data to graph
pixel_endpoint = f'{pixela_endpoint}{USERNAME}/graphs/{graphID}'

pixel_config = {
    'quantity': "1",
    'date': today
}
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=header)
print(response.text)




