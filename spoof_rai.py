import requests
import json

# TODO Get time and loop over month
# TODO Get catch
req = requests.get(
    'https://www.raiplay.it/palinsesto/app/rai-1/05-05-2021.json')

json_data = json.loads(req.text)

clean_data = {
    'channel': json_data['channel'],
    'date': json_data['date'],
    'events': json_data['events']
}

with open('rai_clean.json', 'w') as fp:
    json.dump(clean_data, fp)
