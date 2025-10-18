# WebSocket Control Panel

A complete WebSocket server with web client for controlling color, numbers, and shapes remotely.

## 🚀 Quick Start

### Start Everything (Recommended)
```bash
./start_servers.sh
```

This single command will:
- ✅ Check all dependencies
- ✅ Kill any conflicting processes
- ✅ Start WebSocket server (port 8765)
- ✅ Start HTTP server (port 8000)
- ✅ Show you how to connect from your phone
- ✅ Display live logs
- ✅ Automatically clean up on exit (Ctrl+C)

### Stop Everything
```bash
./stop_servers.sh
```

Or just press `Ctrl+C` if `start_servers.sh` is running.

## 📱 Access from Your Phone

1. Make sure your phone is on the **same WiFi network**
2. Run `./start_servers.sh`
3. On your phone's browser, go to the URL shown (e.g., `http://10.13.0.55:8000/web_client.html`)
4. Click the **"Connect"** button
5. Start controlling!

## 💻 Access from Computer

### Web Interface
```bash
./start_servers.sh
# Then open: http://localhost:8000/web_client.html
```

### Python Client
```bash
python3 client_example.py
```

### Get Current Data
```bash
python3 get_data.py
```

## 📂 Project Structure

```
.
├── start_servers.sh          # 🎯 Main script - run this!
├── stop_servers.sh           # Stop all servers
├── websocket_server.py       # WebSocket server backend
├── start_http_server.py      # HTTP server for web client
├── web_client.html           # Web interface
├── client_example.py         # Python client example
├── get_data.py              # Get current data script
└── README.md                # This file
```

## 🎮 Available Actions

### Set Operations
- **set_color**: Set color to `'blue'` or `'red'`
- **set_number**: Set number to `9`, `6`, `5`, or `3`
- **set_shapes**: Set number of cubes and triangles

### Get Operations
- **get_color**: Get the stored color
- **get_number**: Get the stored number
- **get_shapes**: Get the stored shapes
- **get_all**: Get all stored data

## 🔧 Manual Server Management

### Start WebSocket Server Only
```bash
python3 websocket_server.py
```

### Start HTTP Server Only
```bash
python3 start_http_server.py
```

## 📊 View Logs

When using `start_servers.sh`, logs are saved to:
- `websocket.log` - WebSocket server logs
- `http.log` - HTTP server logs

View in real-time:
```bash
tail -f websocket.log
tail -f http.log
```

## 🌐 Network Configuration

- **WebSocket Server**: `ws://0.0.0.0:8765` (accessible from network)
- **HTTP Server**: `http://0.0.0.0:8000` (accessible from network)

Your local IP will be automatically detected and displayed when you run `./start_servers.sh`.

## 📋 Requirements

- Python 3.7+
- websockets library: `pip install websockets`

## 🐛 Troubleshooting

### Port Already in Use
The script automatically kills processes on ports 8765 and 8000. If you still have issues:
```bash
./stop_servers.sh
./start_servers.sh
```

### Can't Connect from Phone
1. Ensure phone is on the same WiFi network
2. Check firewall settings
3. Verify the IP address shown in the script output
4. Try accessing from computer first: `http://localhost:8000/web_client.html`

### WebSocket Connection Failed
1. Make sure WebSocket server is running
2. Check `websocket.log` for errors
3. Verify the IP address in the web client matches your server IP

## 📝 Example Usage

### Web Client
1. Run `./start_servers.sh`
2. Open browser to the URL shown
3. Click "Connect"
4. Use the interface to set/get values

### Python Client
```python
import asyncio
import websockets
import json

async def test():
    async with websockets.connect("ws://localhost:8765") as ws:
        # Set color
        await ws.send(json.dumps({"action": "set_color", "value": "blue"}))
        response = await ws.recv()
        print(response)
        
        # Get all data
        await ws.send(json.dumps({"action": "get_all"}))
        response = await ws.recv()
        print(response)

asyncio.run(test())
```

## 🎯 Features

- ✅ Real-time WebSocket communication
- ✅ Web-based control panel
- ✅ Python client example
- ✅ Network access from any device
- ✅ Automatic server management
- ✅ Graceful shutdown handling
- ✅ Live logging
- ✅ Error handling and validation

## 📄 License

MIT License - Feel free to use and modify!

---

**Made with ❤️ for ENSI**
