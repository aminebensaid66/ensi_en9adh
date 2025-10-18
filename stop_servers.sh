#!/bin/bash
# Stop all WebSocket and HTTP servers

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Stopping all servers...${NC}"

# Kill WebSocket servers
WS_PIDS=$(pgrep -f "python3.*websocket_server.py")
if [ ! -z "$WS_PIDS" ]; then
    echo -e "${RED}Killing WebSocket servers (PIDs: $WS_PIDS)${NC}"
    kill -9 $WS_PIDS 2>/dev/null
else
    echo "No WebSocket servers running"
fi

# Kill HTTP servers
HTTP_PIDS=$(pgrep -f "python3.*start_http_server.py")
if [ ! -z "$HTTP_PIDS" ]; then
    echo -e "${RED}Killing HTTP servers (PIDs: $HTTP_PIDS)${NC}"
    kill -9 $HTTP_PIDS 2>/dev/null
else
    echo "No HTTP servers running"
fi

# Kill any process on our ports
if command -v lsof &> /dev/null; then
    for port in 8765 8000; do
        PIDS=$(lsof -ti:$port 2>/dev/null)
        if [ ! -z "$PIDS" ]; then
            echo -e "${RED}Killing process on port $port (PIDs: $PIDS)${NC}"
            kill -9 $PIDS 2>/dev/null
        fi
    done
fi

sleep 1
echo -e "${GREEN}All servers stopped!${NC}"
