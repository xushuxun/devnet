#coding: utf-8

from web3 import Web3
import websockets
import json
import asyncio

WS_ENDPOINT = "ws://127.0.0.1:8546"

async def main():
    subscription = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_subscribe",
        "params": ["logs", {}]  # 空字典表示不使用任何过滤器，监听所有事件
    }

    async with websockets.connect(WS_ENDPOINT) as ws:
        await ws.send(json.dumps(subscription))
        subscription_response = await ws.recv()
        print(f"Subscription response: {subscription_response}")

        while True:
            try:
                msg = await asyncio.wait_for(ws.recv(), timeout=60 * 10)
                event = json.loads(msg)
                print(f"New event: {json.dumps(event, indent=2)}")
            except asyncio.TimeoutError:
                print("No events received in the last 10 minutes")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())