import json
import pprint
import time
import requests
import pandas as pd
import websocket

try:
    import thread
except ImportError:
    import _thread as thread


def on_message(ws, message):
    trade = json.loads(message)
    uri="http://0.0.0.0:7500/ticker/eth"
    headers={"Content-Type":"application/json"}
    data={"pair": trade[1]["event"], "price": float(trade[1]["LA"])}
    print(data)
    requests.post(url=uri,headers=headers,json=data)
    # pprint.pprint(data[1]["LA"])


def on_error(ws, error):
    print("...")


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        time.sleep(1)
        message = [
            151,
            {
                "type": 402,
                "channel": 'ticker',
                "event": 'ETHTRY',
                "join": True,
            }
        ]
        # print("MESSAGE: ", message[1])
        ws.send(json.dumps(message))
    thread.start_new_thread(run, ())



if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://ws-feed-pro.btcturk.com/",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
