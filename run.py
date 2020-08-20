import DashApp.index # load the layout by importing
from DashApp.app import app

import argparse

from aot_api.data_fetcher import getData

parser = argparse.ArgumentParser()

parser.add_argument("-debug", '--d', help="Whether or not to run the server in debug mode or not. Defaults to True.", 
                    default=True, dest="debug")

parser.add_argument("-hot_reload", '--r', help="If this setting is enabled, when you change the program code, the dashboard reloads automatically. Defaults to true.",
                    default=True, dest="hot_reload")

parser.add_argument('-project', "--p", help="The project to retrieve node data from.", default="chicago", dest="project_slug")

parser.add_argument('-verbose', '--v', help="Whether or not to print out the data retrieved from the API", dest="verbose", action="store_true")

args = parser.parse_args()

print("Getting data...")
getData(project_slug=args.project_slug, verbose=args.verbose) # get the data ahead of time and make sure it's cached so the callback doesn't take forever.
print("Data retrieved!")
print("Starting the dash server...")

app.run_server(debug=args.debug, dev_tools_hot_reload=False, use_reloader=False)