
import json

SETTINGS = json.load(open("../resources/settings.json", "rb"))
APP_NAME = SETTINGS["APP_NAME"]
MY_MODELS = SETTINGS["MY_MODELS"]

from flask import Flask
app = Flask(__name__)

def page_not_found(e):
  return f'You may want to go <a href="{APP_NAME}">here</a>.', 404

def prefix_route(route_function, prefix='', mask='{0}{1}'):
    '''
    Defines a new route function with a prefix.
    The mask argument is a `format string` formatted with, in that order:
    prefix, route
    '''
    def newroute(route, *args, **kwargs):
        '''New function to prefix the route'''
        return route_function(mask.format(prefix, route), *args, **kwargs)
    return newroute

app.route = prefix_route(app.route, f'/{APP_NAME.replace(" ","_")}')
app.register_error_handler(404, page_not_found)

from main import loadmodels
models = loadmodels(MY_MODELS, resource="../resources")

from routes import create_routes
create_routes(app, models)
print(app.url_map)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8484, debug=False)
