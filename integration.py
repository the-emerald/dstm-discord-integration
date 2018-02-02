import rpc
import time
import requests
import json

def fetch_data():
    try:
        page = requests.post("http://127.0.0.1:2222/jsonrpc")
        data = page.json() # This will most likely never work
        can_post_normally = True
    except Exception as e:
        # Because requests doesn't like what DSTM outputs and always throws a BadStatusLine,
        # we'll just catch every single exception here - by doing string manipulation later
        # it'll be clear if JSON was passed or some garbage.
        message = str(e)
        can_post_normally = False

    if not can_post_normally:
        try:
            data = message.split("(")[2][1:-6]
        except Exception:
            print("Can't find DSTM telemetry data! Are you sure the --telemetry flag is set on the miner? Is the miner on?")
            quit()

    return data

client_id = '405940771791962121' #Your application's client ID as a string. (This isn't a real client ID)
RPC = rpc.DiscordRPC(client_id) #Send the client ID to the rpc module
try:
    RPC.start() #Start the RPC connection
    print("RPC Connection Success.")
except FileNotFoundError:
    print("Error: Discord has not been started yet. Please make sure Discord is active.")
    quit()
time.sleep(5)
while True:
    data = json.loads(fetch_data())
    #print(data['result'])
    #print(data['result'][0]['gpu_id'])
    activity = {
            "state": "Mining on " + data["server"],
            "details": "Speed: " + str(data["result"][0]["avg_sol_ps"]),
            "timestamps": {
                "start": data["uptime"]
            },
            "assets": {
                "small_text": "Text for small_image",
                "small_image": "img_small",
                "large_text": "Text for large_image",
                "large_image": "img_large"
            }
        }
    RPC.send_rich_presence(activity)
    print("Rich presence sent.")
    time.sleep(60)