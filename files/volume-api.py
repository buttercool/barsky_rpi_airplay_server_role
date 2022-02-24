from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource, reqparse
import math
import subprocess



app = Flask(__name__)
api = Api(app)

# Define controls used on this node
controls = [
    {
        "name": "vol_up",
        "output": "Digital",
        "increment": 1
    },
    {
        "name": "vol_down",
        "output": "Digital",
        "increment": 1
    },
    {
        "name": "mute_on",
        "output": "Digital",
        "increment": 0
    },
    {
        "name": "mute_off",
        "output": "Digital",
        "increment": 0
    },
    {
        "name": "mute_toggle",
        "output": "Digital",
        "increment": 0
    },
    {
        "name": "vol_disp",
        "output": "Digital",
        "increment": 0
    },
    {
        "name": "mute_disp",
        "output": "Digital",
        "increment": 0
    }
]

class Control(Resource):

    def get(self, name):
        for control in controls:
            if(name == control["name"]):
                # If a matching control is found, then evaluate which one it is
                # And construct an amixer command as needed...
                if(control["name"] == "vol_up"):
                    amixer_cmd = "/usr/bin/amixer set {} {}%+".format(control["output"],str(control["increment"]))
                if(control["name"] == "vol_down"):
                    amixer_cmd = "/usr/bin/amixer set {} {}%-".format(control["output"],str(control["increment"]))
                if(control["name"] == "mute_on"):
                    amixer_cmd = "/usr/bin/amixer set {} mute".format(control["output"])
                if(control["name"] == "mute_off"):
                    amixer_cmd = "/usr/bin/amixer set {} unmute".format(control["output"])
                if(control["name"] == "mute_toggle"):
                    amixer_cmd = "/usr/bin/amixer set {} toggle".format(control["output"])
                if(control["name"] == "vol_disp" or control["name"] == "mute_disp"):
                    skip_cmd = True
                else:
                    skip_cmd = False

                # Now send the actual command unless skipped
                if(skip_cmd != True):
                    send_command = subprocess.check_output(['bash','-c', amixer_cmd])
                
                if(control["name"] == "mute_disp" or control["name"] == "mute_toggle"):
                    # Construct the current mute status command & send it
                    amixer_mute_disp_cmd = "amixer get {} | grep off".format(control["output"])
                    try:
                        mute_result = subprocess.check_output(['bash','-c', amixer_mute_disp_cmd])
                        if mute_result:
                            curr_mute = "muted"
                        else:
                            curr_mute = "not_muted"
                    except:
                        curr_mute = "not_muted"
                    return str(curr_mute), 200, {'Content-Type': 'application/json; charset=utf-8', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS'}

                else:
                    # Construct the current volume command & send it
                    amixer_vol_disp_cmd = "amixer get {} | grep % | awk '{{print $5}}'|sed 's/[^0-9]//g'".format(control["output"])
                    curr_vol = subprocess.check_output(['bash','-c', amixer_vol_disp_cmd]).split()[0]
                    return str(curr_vol.decode()), 200, {'Content-Type': 'application/json; charset=utf-8', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE,OPTIONS'}

# awk
api.add_resource(Control, "/api/control/<string:name>")

app.run(host='0.0.0.0',port=5500)