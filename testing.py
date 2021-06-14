import websockets
import asyncio
import json
import random

uri = 'wss://gateway.discord.gg?v=9&encoding=json'
heartbeat_interval = 0

async def hello():

    async with websockets.connect(uri) as websocket:
        greeting = await websocket.recv()
        
        greeting = json.loads(greeting)
        
        heartbeat_interval = greeting["d"]["heartbeat_interval"]

        print('yes')
        nom = (heartbeat_interval * random.random()) / 1000
        print(nom)
        print(heartbeat_interval/1000)
        await asyncio.sleep(nom)
        
        print('yes')


        while True:
            await websocket.send(json.dumps({"op" : 1, "d" : "null"}))

            res = await websocket.recv()

            if json.loads(res)['op'] == 1:
                await websocket.send(json.dumps({"op" : 1}))

            await asyncio.sleep(heartbeat_interval / 1000)

            await websocket.send(json.dumps({"op" : 1, "d" : "null"}))
            print(res)

        greeting = await websocket.recv()
        # while True:

        # print(greeting)
        
    
asyncio.get_event_loop().run_until_complete(hello())