import asyncio
import websockets
import json


async def get_color():
    """Get the stored color from the WebSocket server"""
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"action": "get_color"}))
            response = await websocket.recv()
            result = json.loads(response)
            if result.get("status") == "success":
                return result.get("data")
            else:
                print(f"Error: {result.get('message')}")
                return None
    except Exception as e:
        print(f"Connection error: {e}")
        return None


async def get_number():
    """Get the stored number from the WebSocket server"""
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"action": "get_number"}))
            response = await websocket.recv()
            result = json.loads(response)
            if result.get("status") == "success":
                return result.get("data")
            else:
                print(f"Error: {result.get('message')}")
                return None
    except Exception as e:
        print(f"Connection error: {e}")
        return None


async def get_shapes():
    """Get the stored shapes from the WebSocket server"""
    uri = "ws://localhost:8765"
    try:
        async with websockets.connect(uri) as websocket:
            await websocket.send(json.dumps({"action": "get_shapes"}))
            response = await websocket.recv()
            result = json.loads(response)
            if result.get("status") == "success":
                return result.get("data")
            else:
                print(f"Error: {result.get('message')}")
                return None
    except Exception as e:
        print(f"Connection error: {e}")
        return None


# Example usage
async def main():
    """Example of how to use the get functions"""
    print("Getting color...")
    color = await get_color()
    print(f"Color: {color}\n")
    
    print("Getting number...")
    number = await get_number()
    print(f"Number: {number}\n")
    
    print("Getting shapes...")
    shapes = await get_shapes()
    print(f"Shapes: {shapes}")
    if shapes:
        print(f"  - Cubes: {shapes.get('cubes')}")
        print(f"  - Triangles: {shapes.get('triangles')}\n")


if __name__ == "__main__":
    asyncio.run(main())
