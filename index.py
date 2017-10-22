from __future__ import division

import statistics
import requests
import api_config
import datetime
import csv

# extract configuration
username = api_config.username
password = api_config.password
auth_token = api_config.auth_token
event_ids = api_config.event_ids

# Prepare information for api requests
login_url = 'https://api.stubhub.com/login'
inventory_url = 'https://api.stubhub.com/search/inventory/v2'

headers = {
        'Content-Type':'application/x-www-form-urlencoded',
        'Authorization':'Basic '+auth_token,}
body = {
        'grant_type':'password',
        'username':username,
        'password':password,
        'scope':'PRODUCTION'}

r = requests.post(login_url, headers=headers, data=body)

token_respoonse = r.json()
access_token = token_respoonse['access_token']
user_GUID = r.headers['X-StubHub-User-GUID']

headers['Authorization'] = 'Bearer ' + access_token
headers['Accept'] = 'application/json'
headers['Accept-Encoding'] = 'application/json'

cur_time = datetime.datetime.now()
csv_rows = []

for event_id in event_ids:
    prices = []

    is_scraping_incomplete = True
    data = {'eventid':event_id, 'rows':250, 'start':1}

    while is_scraping_incomplete:

        inventory = requests.get(inventory_url, headers=headers, params=data)
        inv = inventory.json()
        listings = inv['listing']

        cur_prices = [listing['currentPrice']['amount'] for listing in listings]
        prices = prices + cur_prices

        # Scraping incomplete when results returned are less than the max returned
        is_scraping_incomplete = len(cur_prices) == 250

        # advance the starting position for the results
        data['start'] = data['start'] + 250

    csv_rows.append([cur_time, min(prices), max(prices),
        sum(prices)/len(prices), statistics.median(prices), event_id])

try:
    open('prices.csv')
except:
    header_row = ['time', 'min', 'max', 'avg', 'median', 'event']
    csv_rows.insert(0, header_row)

with open('prices.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerows(csv_rows)
