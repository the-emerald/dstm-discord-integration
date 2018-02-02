import rpc
import time
import requests
import json

def fetch_data():
    try:
        page = requests.post("http://127.0.0.1:2222/jsonrpc")
        data = page.json() # This will most likely never work
    except Exception as e:
        # Because requests doesn't like what DSTM outputs and always throws a BadStatusLine,
        # we'll just catch every single exception here - by doing string manipulation later
        # it'll be clear if JSON was passed or some garbage.
        message = str(e)
    try:
        data = message.split("(")[2][1:-6]
        return data
    except Exception:
        print("Can't find DSTM telemetry data! Are you sure the --telemetry flag is set on the miner? Is the miner on?")
        quit()

print("DSTM Miner Integration for Discord")
print("Written by suclearnub\n")
client_id = '405940771791962121' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("RPC connection successful.")

time.sleep(5)
start_time = time.time()
while True:
    try:
        data = json.loads(fetch_data())
    except Exception:
        print("Can't find DSTM telemetry data! Are you sure the --telemetry flag is set on the miner? Is the miner on?")
        quit()
    activity = {
            "state": "Mining on " + data["server"],
            "details": "Speed: " + "{:.0f}".format(data["result"][0]["avg_sol_ps"]) + " Sol/s",
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "large_text": "Hard at work!",
                "large_image": "mining"
            }
        }
    rpc_obj.set_activity(activity)
    time.sleep(30)