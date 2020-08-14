import DashApp.index # load the layout by importing
from DashApp.app import app

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-debug", '--d', help="Whether or not to run the server in debug mode or not. Defaults to True.", 
                    default=True, dest="debug")

parser.add_argument("-hot_reload", '--r', help="If this setting is enabled, when you change the program code, the dashboard reloads automatically. Defaults to true.",
                    default=True, dest="hot_reload")

args = parser.parse_args()

app.run_server(debug=args.debug, dev_tools_hot_reload=args.hot_reload, use_reloader=args.hot_reload)