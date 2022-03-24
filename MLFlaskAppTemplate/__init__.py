import os
from .templates import *

def template(app_name="ML Template App", destination="."):
    des = os.path.join(destination, app_name)
    if not os.path.exists(des):
        os.mkdir(des)
    print(f"Creating files in {os.path.abspath(des)}")
    flasksite = os.path.join(des, "flasksite")
    if not os.path.exists(flasksite):
        os.mkdir(flasksite)
    resources = os.path.join(des, "resources")    
    if not os.path.exists(resources):
        os.mkdir(resources)
    os.chdir(flasksite)
    print(f"./{os.path.basename(os.getcwd())}/app.py")
    with open("app.py", "w+") as f:
        f.write(generate_app())
    print(f"./{os.path.basename(os.getcwd())}/main.py")
    with open("main.py", "w+") as f:
        f.write(generate_main())
    print(f"./{os.path.basename(os.getcwd())}/routes.py")
    with open("routes.py", "w+") as f:
        f.write(generate_routes())
    os.chdir("../resources")
    print(f"./{os.path.basename(os.getcwd())}/settings.json")
    with open("settings.json", "w+") as f:
        f.write(generate_settings(app_name))
