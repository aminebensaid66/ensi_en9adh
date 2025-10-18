import asyncio
import websockets
import json


async def test_websocket():
    """Example client to test the WebSocket server"""
    uri = "ws://localhost:8765"
    
    async with websockets.connect(uri) as websocket:
        print("Connected to WebSocket server\n")
        
        # Set color to blue
        print("Setting color to 'blue'...")
        await websocket.send(json.dumps({"action": "set_color", "value": "blue"}))
        response = await websocket.recv()
        print(f"Response: {response}\n")
        
        # Set number to 9
        print("Setting number to 9...")
        await websocket.send(json.dumps({"action": "set_number", "value": 9}))
        response = await websocket.recv()
        print(f"Response: {response}\n")
        
        # Set shapes (5 cubes, 3 triangles)
        print("Setting shapes: 5 cubes, 3 triangles...")
        await websocket.send(json.dumps({"action": "set_shapes", "cubes": 5, "triangles": 3}))
        response = await websocket.recv()
        print(f"Response: {response}\n")
        
        # Get color
        print("Getting color...")
        await websocket.send(json.dumps({"action": "get_color"}))
        response = await websocket.recv()
        print(f"Response: {response}\n")
        
        # Get number
        print("Getting number...")
        await websocket.send(json.dumps({"action": "get_number"}))
        response = await websocket.recv()
        print(f"Response: {response}\n")
        
        # Get shapes
        print("Getting shapes...")
        await websocket.send(json.dumps({"action": "get_shapes"}))
        response = await websocket.recv()
        print(f"Response: {response}\n")
        
        # Get all data
        print("Getting all data...")
        await websocket.send(json.dumps({"action": "get_all"}))
        response = await websocket.recv()
        print(f"Response: {response}\n")


if __name__ == "__main__":
    asyncio.run(test_websocket())
