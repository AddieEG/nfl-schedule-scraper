# %%
#-------------------
#imports
import json
import pandas as pd
import datetime
from datetime import timedelta
import os
#-------------------

# %%
#-------------------
#adding markets to the json
#splitting up the additions to the json 
#this just adds the markets to thhe game['broadcast'] dictionary and game['home']['market'] and game['away']['market'] dictionaries

#Change according to your path
csv_data1 = '/Users/adelaidegilley/Downloads/ZoomphCRS/nfl/nfl-data/NFL_market_broadcastcsv.csv'
csv_data = pd.read_csv(csv_data1)


team_market_mapping = dict(zip(csv_data['Team'], csv_data['Market']))

# Specify the JSON file path
json_file_path = '/Users/adelaidegilley/Downloads/ZoomphCRS/nfl/nfl-data'

# Read the JSON file
with open(os.path.join(json_file_path, 'NFLSchedulePre2023.json'), 'r') as file:
    data = json.load(file)



for week in data['weeks']:
    for game in week['games']:
        home_team_name = game['home']['name']
        away_team_name = game['away']['name']
        
        if home_team_name in team_market_mapping:
            game['home']['market'] = team_market_mapping[home_team_name]
        
        if away_team_name in team_market_mapping:
            game['away']['market'] = team_market_mapping[away_team_name]

        if 'broadcast' not in game:
            game['broadcast'] = {}
        
        # Update the broadcast dictionary with home and away markets
        game['broadcast']['homemarket'] = game['home']['market']
        game['broadcast']['awaymarket'] = game['away']['market']

# Specify the new JSON file name
new_json_file_name = 'NFLSchedulePre2023-2.json'

# Construct the path for the new JSON file
new_json_file_path = os.path.join(json_file_path, new_json_file_name)

# Save the data to the new JSON file
with open(new_json_file_path, 'w') as file:
    json.dump(data, file, indent=4)
#-------------------
# %%
#-------------------
#this second part adds the call sign and channel id from the csv to the json file, it passes any cases there is no network because some preseason games didnt indicate one
# Specify the JSON file path, change accordingly
json_file_path = '/Users/adelaidegilley/Downloads/ZoomphCRS/nfl/nfl-data'

# Read the JSON file
with open(os.path.join(json_file_path, 'NFLSchedulePre2023-2.json'), 'r') as json_file:
    data = json.load(json_file)

# Loop through the JSON data
for week in data['weeks']:
    for game in week['games']:
        broadcast = game.get('broadcast', {})
        network = broadcast.get('network')
        
        if network:
            home_market = game['home']['market']

            # Filter the Excel data based on conditions
            matching_rows_home = csv_data[(csv_data['Market'] == home_market) & (csv_data['Affiliate'] == network)]
            matching_rows_away = csv_data[(csv_data['Market'] == game['away']['market']) & (csv_data['Affiliate'] == network)]

            if not matching_rows_home.empty:
                home_call_sign = matching_rows_home['Call_Sign'].iloc[0]
                home_channel_id = matching_rows_home['Channel_ID'].iloc[0]

                broadcast['homecallsign'] = home_call_sign
                broadcast['homechannelid'] = home_channel_id

            if not matching_rows_away.empty:
                away_call_sign = matching_rows_away['Call_Sign'].iloc[0].replace('\u200b', '')  # Remove U+200B
                away_channel_id = matching_rows_away['Channel_ID'].iloc[0]

                broadcast['awaycallsign'] = away_call_sign
                broadcast['awaychannelid'] = away_channel_id
        else:
            # Add homemarket and awaymarket even if network is missing
            broadcast['homemarket'] = game['home']['market']
            broadcast['awaymarket'] = game['away']['market']

# Save the modified JSON data
with open(os.path.join(json_file_path, 'NFLSchedulePre2023-2.json'), 'w') as json_file:
    json.dump(data, json_file, indent=4)
#-------------------

# %%
#-------------------
#change filepath to your own 
filepath = '/Users/adelaidegilley/Downloads/ZoomphCRS/nfl/nfl-data/NFLSchedulePre2023-2.json'

def load_nfl_pre_full(filepath):
    pre_list = []

    with open(filepath, "r") as file:
        for line in file:
            # Append each line to the list after removing any leading/trailing whitespace
            pre_list.append(line.strip())

    # Join the list elements into a single string
    json_string = ''.join(pre_list)

    # Parse the JSON string into a Python dictionary
    nfl_pre_dict = json.loads(json_string)

    return nfl_pre_dict
#-------------------
# %%
#-------------------
nfl_pre_dict = load_nfl_pre_full(filepath)
#-------------------
# %%
#-------------------
#this chunk scrapes the data from the json file, specifically NFLSchedulePre2023-2.json
# Subtracts 30 minutes from a date time string in YYYY-MM-DD HH:MM:SS format
def subtract30minutes(date_string):
    date_format = '%Y-%m-%d %H:%M:%S'
    date_time = datetime.datetime.strptime(date_string, date_format)
    new_date_time = date_time - timedelta(minutes=30)
    return new_date_time.strftime(date_format)

# Adds 210 minutes (3.5 hours) to a date time string in YYYY-MM-DD HH:MM:SS format
def add210minutes(date_string):
    date_format = '%Y-%m-%d %H:%M:%S'
    date_time = datetime.datetime.strptime(date_string, date_format)
    new_date_time = date_time + timedelta(minutes=210)
    return new_date_time.strftime(date_format)

# Starts at 0 for the Hall of Fame Game
week_number = int(input("Input week #: "))
games = nfl_pre_dict["weeks"][week_number]["games"]

# Create an empty list to store the extracted data
game_details = []

for game in games:
    # Splitting date and time
    scheduled_datetime_str = game["scheduled"]
    scheduled_date_str, scheduled_time_with_offset = scheduled_datetime_str.split('T')
    scheduled_date_obj = datetime.datetime.fromisoformat(scheduled_date_str)

    # Splitting time and timezone offset
    scheduled_time, timezone_offset = scheduled_time_with_offset[:-6], scheduled_time_with_offset[-6:]

    scheduled_time_obj = datetime.time.fromisoformat(scheduled_time)

    scheduled_date = scheduled_date_obj.date()
    scheduled_time = scheduled_time_obj.strftime("%H:%M:%S")

    # Subtract 30 minutes from the scheduled_time
    adjusted_start_time = subtract30minutes(f"{scheduled_date_str} {scheduled_time}")

    end_time = add210minutes(f"{scheduled_date_str} {scheduled_time}")
    venue = game["venue"]["name"]
    city = game["venue"]["city"]
    state = game["venue"]["state"]
    location = f"{venue}, {city}, {state}"
    home_team = game["home"]["name"]
    away_team = game["away"]["name"]
    home_market = game["broadcast"]["homemarket"]
    away_market = game["broadcast"]["awaymarket"]
    
    home_channel_id = game["broadcast"]["homechannelid"] if "homechannelid" in game["broadcast"] else ""
    away_channel_id = game["broadcast"]["awaychannelid"] if "awaychannelid" in game["broadcast"] else ""
    
    broadcast_channel = game["broadcast"]["network"] if "network" in game["broadcast"] else ""
    
    home_call_sign = game["broadcast"]["homecallsign"] if "homecallsign" in game["broadcast"] else ""
    away_call_sign = game["broadcast"]["awaycallsign"] if "awaycallsign" in game["broadcast"] else ""
    
    home_call_sign = home_call_sign.rstrip('_')
    away_call_sign = away_call_sign.rstrip('_')
    
    sport = "Football"
    game_details.append([week_number, location, broadcast_channel, home_market, home_call_sign, home_channel_id, adjusted_start_time, end_time, sport, home_team, away_team])
    # Append away market details
    game_details.append([week_number, location, broadcast_channel, away_market, away_call_sign, away_channel_id, adjusted_start_time, end_time, sport, home_team, away_team])

# Create a pandas DataFrame from the list of game details
df = pd.DataFrame(game_details, columns=["Week", "Location", "Parent Channel", "Market", "Call Sign", "Channel ID", "Start Time", "End Time", "Sport", "Home Team", "Away Team"])

# Print the DataFrame
#print(df)

# Save the DataFrame to a CSV file
#df.to_csv(f"NFLPreseasonWeek{week_number}.csv", index=False)
df.to_csv("Preseason-Schedules/NFLPreseasonWeek{}.csv".format(week_number), index=False)
#-------------------



# %%
