import requests
from collections import defaultdict
from string import Template
from config import read_config

# POSTMAN DOCS: https://documenter.getpostman.com/view/664302/S1ENwy59#3d2a17c1-2129-475c-b4c8-7d362d6000cd
URL_TEMPLATE = Template('https://api.ebird.org/v2/data/obs/$overall_location/recent')

config = read_config()

# gets raw responses from call to eBird API. Structure of response can be found here https://documenter.getpostman.com/view/664302/S1ENwy59#3d2a17c1-2129-475c-b4c8-7d362d6000cd
def __get_all_observations(overall_location, specific_locations):
    headers = {'X-eBirdApiToken': config['ebirdapitoken']}
    if specific_locations:
        params = {'r': specific_locations}
    response = requests.get(URL_TEMPLATE.substitute(overall_location=overall_location), params=params, headers=headers)
    if response.status_code != 200:
        raise f'got status code {response.status_code}, expected 200'
    return response.json()

# get counts from all observations over the last two weeks at the specified overall location
def get_counts(overall_location, specific_locations=None):
    all_observations = __get_all_observations(overall_location, specific_locations)
    observations_per_bird = defaultdict(list)
    for observation in all_observations:
        observations_per_bird[observation["comName"]].append(observation)
    
    counts = {}
    for bird_name, observations in observations_per_bird.items():
        counts[bird_name] = sum([o.get('howMany', 0) for o in observations])

    return counts

# gets the list of seen bird sorted most common to least common
# TODO see if I can filter by verified sightings
counts = get_counts(config['locations']['chicago'], config['locations']['monstrose-all'])
print(sorted(counts.items(), key=lambda kv: kv[1], reverse=True))