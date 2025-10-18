# WebSocket Server with Data Storage

This project implements a WebSocket server that allows you to:

- Set and get color (blue or red)
- Set and get number (9, 6, 5, or 3)
- Set and get shapes (number of cubes and triangles)

## Files

- `websocket_server.py` - The main WebSocket server
- `client_example.py` - Python client example
- `web_client.html` - HTML/JavaScript web client with UI

## Installation

First, install the required dependency:

```bash
pip install websockets
```

## Usage

### 1. Start the Server

```bash
python websocket_server.py
```

The server will start on `ws://localhost:8765`

### 2. Use the Web Client

Open `web_client.html` in your web browser. It will automatically connect to the server and provide a user interface to:

- Select and set colors
- Select and set numbers
- Input and set shapes (cubes and triangles)
- Retrieve all stored data

### 3. Use the Python Client (Optional)

In another terminal, run:

```bash
python client_example.py
```

## API Reference

The server accepts JSON messages with the following actions:

### Set Color

```json
{ "action": "set_color", "value": "blue" }
```

or

```json
{ "action": "set_color", "value": "red" }
```

### Set Number

```json
{ "action": "set_number", "value": 9 }
```

Valid values: 9, 6, 5, or 3

### Set Shapes

```json
{ "action": "set_shapes", "cubes": 5, "triangles": 3 }
```

### Get Color

```json
{ "action": "get_color" }
```

### Get Number

```json
{ "action": "get_number" }
```

### Get Shapes

```json
{ "action": "get_shapes" }
```

### Get All Data

```json
{ "action": "get_all" }
```

## Response Format

All responses are in JSON format:

Success response:

```json
{"status": "success", "message": "...", "data": ...}
```

Error response:

```json
{ "status": "error", "message": "..." }
```
# ensi_en9adh
