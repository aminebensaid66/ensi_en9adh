import asyncio
import websockets
import json
from typing import Optional, Dict

class DataStore:
    """Store for color, number, and shapes data"""
    def __init__(self):
        self.color: Optional[str] = None
        self.number: Optional[int] = None
        self.shapes: Dict[str, int] = {"cubes": 0, "triangles": 0}
    
    def set_color(self, color: str) -> bool:
        """Set color (blue or red)"""
        if color.lower() in ["blue", "red"]:
            self.color = color.lower()
            return True
        return False
    
    def set_number(self, number: int) -> bool:
        """Set number (9, 6, 5, or 3)"""
        if number in [9, 6, 5, 3]:
            self.number = number
            return True
        return False
    
    def set_shapes(self, cubes: int, triangles: int) -> bool:
        """Set the number of cubes and triangles"""
        if cubes >= 0 and triangles >= 0:
            self.shapes["cubes"] = cubes
            self.shapes["triangles"] = triangles
            return True
        return False
    
    def get_color(self) -> Optional[str]:
        """Get the stored color"""
        return self.color
    
    def get_number(self) -> Optional[int]:
        """Get the stored number"""
        return self.number
    
    def get_shapes(self) -> Dict[str, int]:
        """Get the stored shapes"""
        return self.shapes.copy()
    
    def get_all_data(self) -> Dict:
        """Get all stored data"""
        return {
            "color": self.color,
            "number": self.number,
            "shapes": self.shapes.copy()
        }


# Global data store
data_store = DataStore()


async def handle_client(websocket, path):
    """Handle WebSocket client connections"""
    print(f"Client connected from {websocket.remote_address}")
    
    try:
        async for message in websocket:
            try:
                # Parse the incoming JSON message
                data = json.loads(message)
                action = data.get("action")
                
                response = {"status": "error", "message": "Unknown action"}
                
                # Handle different actions
                if action == "set_color":
                    color = data.get("value")
                    if data_store.set_color(color):
                        response = {"status": "success", "message": f"Color set to {color}"}
                    else:
                        response = {"status": "error", "message": "Invalid color. Choose 'blue' or 'red'"}
                
                elif action == "set_number":
                    number = data.get("value")
                    if data_store.set_number(number):
                        response = {"status": "success", "message": f"Number set to {number}"}
                    else:
                        response = {"status": "error", "message": "Invalid number. Choose 9, 6, 5, or 3"}
                
                elif action == "set_shapes":
                    cubes = data.get("cubes", 0)
                    triangles = data.get("triangles", 0)
                    if data_store.set_shapes(cubes, triangles):
                        response = {"status": "success", "message": f"Shapes set to {cubes} cubes and {triangles} triangles"}
                    else:
                        response = {"status": "error", "message": "Invalid shapes. Both values must be >= 0"}
                
                elif action == "get_color":
                    color = data_store.get_color()
                    response = {"status": "success", "data": color}
                
                elif action == "get_number":
                    number = data_store.get_number()
                    response = {"status": "success", "data": number}
                
                elif action == "get_shapes":
                    shapes = data_store.get_shapes()
                    response = {"status": "success", "data": shapes}
                
                elif action == "get_all":
                    all_data = data_store.get_all_data()
                    response = {"status": "success", "data": all_data}
                
                # Send response back to client
                await websocket.send(json.dumps(response))
                
            except json.JSONDecodeError:
                error_response = {"status": "error", "message": "Invalid JSON format"}
                await websocket.send(json.dumps(error_response))
            except Exception as e:
                error_response = {"status": "error", "message": str(e)}
                await websocket.send(json.dumps(error_response))
    
    except websockets.exceptions.ConnectionClosed:
        print(f"Client {websocket.remote_address} disconnected")


async def main():
    """Start the WebSocket server"""
    host = "localhost"
    port = 8765
    
    print(f"Starting WebSocket server on ws://{host}:{port}")
    print("\nAvailable actions:")
    print("  - set_color: Set color to 'blue' or 'red'")
    print("  - set_number: Set number to 9, 6, 5, or 3")
    print("  - set_shapes: Set number of cubes and triangles")
    print("  - get_color: Get the stored color")
    print("  - get_number: Get the stored number")
    print("  - get_shapes: Get the stored shapes")
    print("  - get_all: Get all stored data")
    print("\nWaiting for connections...\n")
    
    async with websockets.serve(handle_client, host, port):
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
