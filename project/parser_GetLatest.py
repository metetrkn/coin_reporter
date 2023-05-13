import json
import csv
from datetime import datetime

# Load the JSON data
with open('./get_latest.json') as f:
    data = json.load(f)

# Create a CSV file
with open('./output2.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # defining global ID list to extract id's of curruncies listed in Getting Latest request
    global ID
    curr_ids = []

    # caching timestamp once for perfomance
    timestamp = datetime.strptime(data['status']['timestamp'],
                                  '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')

    # Write the header row
    writer.writerow(['', '', '', '', '','', '', '','', '','','', '', '', '','', ''])
                    # 'Last 7 Days' add if you can find related data

    # Loop through each item in the 'data' array
    for item in data['data']:
        # Extract the data we want
        id = item['id']
        name = item['name']
        symbol = item['symbol']
        price = round(item['quote']['USD']['price'], 2)
        market_cap = int(round(item['quote']['USD']['market_cap'], 0))
        market_cap_dom = round(item['quote']['USD']['market_cap_dominance'], 2)
        circ_supply = item['circulating_supply']
        is_infinite = item["infinite_supply"]
        volume_24 = int(round(item['quote']['USD']['volume_24h'], 0))
        percent_change_1h = round(item['quote']['USD']['percent_change_1h'], 2)
        per_change_24h = round(item['quote']['USD']['percent_change_24h'], 2)
        per_change_7d = round(item['quote']['USD']['percent_change_7d'], 2)
        per_change_30d = round(item['quote']['USD']['percent_change_30d'], 2)
        per_change_60d = round(item['quote']['USD']['percent_change_60d'], 2)
        per_change_90d = round(item['quote']['USD']['percent_change_90d'], 2)
        # last_7_days = (if you can find related data)

        # Getting Id's to parse into MetaData v1(deprecated) get request
        curr_ids.append(id)

        # Write the data to the CSV file
        writer.writerow(['', id, timestamp, name, symbol, price, market_cap, market_cap_dom,
                         circ_supply, is_infinite, volume_24, percent_change_1h, per_change_24h,
                           per_change_7d, per_change_30d, per_change_60d, per_change_90d])
                         #open_value, low_day, high_day, close_value, last_7_days

# Extracting Id's of coins in list to a txt file in MetaData v1(deprecated)                      
with open("./curr_ids.txt", 'w', newline='') as f:
    # removing [...] curly braces from id output
    all_ids = str(curr_ids)[1:-1]
    # removing spaces between ids
    all_ids = all_ids.replace(" ", "")
    f.write(all_ids)

