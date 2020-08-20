import DashApp.index # load the layout by importing
from DashApp.app import app

import argparse

from aot_api.data_fetcher import getData

parser = argparse.ArgumentParser()

parser.add_argument("-debug", '--d', help="Whether or not to run the server in debug mode or not. Defaults to True.", 
                    default=True, dest="debug")

parser.add_argument("-hot_reload", '--r', help="If this setting is enabled, when you change the program code, the dashboard reloads automatically. Defaults to true.",
                    default=True, dest="hot_reload")

args = parser.parse_args()

print("Getting data...")
getData() # get the data ahead of time and make sure it's cached so the callback doesn't take forever.
print("Data retrieved!")
print("Starting the dash server...")

app.run_server(debug=args.debug, dev_tools_hot_reload=False, use_reloader=False)