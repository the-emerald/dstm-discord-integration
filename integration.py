import rpc
import time
import requests

client_id = '405940771791962121' #Your application's client ID as a string. (This isn't a real client ID)
RPC = rpc.DiscordRPC(client_id) #Send the client ID to the rpc module
RPC.start() #Start the RPC connection


try:
    page = requests.get("127.0.0.1:2222")
except Exception:
    print("Can't find DSTM telemetry server! Are you sure the --telemetry flag is set on the miner?")
    quit()
data = page.json()
while True:
    activity = {
            "state": "Mining on " + data["server"],
            "details": "Speed: " + data["result"]["avg_sol_ps"],
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
    time.sleep(60)