#!/bin/bash
# Complete server management script for WebSocket and HTTP servers

# Color codes for pretty output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Get local IP address
LOCAL_IP=$(hostname -I | awk '{print $1}')
WS_PORT=8765
HTTP_PORT=8000

# Function to print colored messages
print_info() {
    echo -e "${CYAN}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Function to check if port is in use
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        return 0  # Port is in use
    else
        return 1  # Port is free
    fi
}

# Function to kill process on port
kill_port() {
    local port=$1
    local pids=$(lsof -ti:$port 2>/dev/null)
    if [ ! -z "$pids" ]; then
        print_warning "Killing existing process on port $port..."
        kill -9 $pids 2>/dev/null
        sleep 1
    fi
}

# Function to cleanup on exit
cleanup() {
    echo ""
    print_warning "Shutting down servers..."
    
    # Kill WebSocket server
    if [ ! -z "$WS_PID" ] && kill -0 $WS_PID 2>/dev/null; then
        kill $WS_PID 2>/dev/null
        print_info "WebSocket server stopped (PID: $WS_PID)"
    fi
    
    # Kill HTTP server
    if [ ! -z "$HTTP_PID" ] && kill -0 $HTTP_PID 2>/dev/null; then
        kill $HTTP_PID 2>/dev/null
        print_info "HTTP server stopped (PID: $HTTP_PID)"
    fi
    
    # Kill any remaining processes on our ports
    kill_port $WS_PORT
    kill_port $HTTP_PORT
    
    print_success "All servers stopped. Goodbye!"
    exit 0
}

# Set up trap to catch Ctrl+C and other termination signals
trap cleanup SIGINT SIGTERM EXIT

# Main script starts here
clear
echo "═══════════════════════════════════════════════════════"
echo -e "${CYAN}    WebSocket & HTTP Server Manager${NC}"
echo "═══════════════════════════════════════════════════════"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    print_error "Python3 is not installed!"
    exit 1
fi

# Check if required files exist
if [ ! -f "websocket_server.py" ]; then
    print_error "websocket_server.py not found!"
    exit 1
fi

if [ ! -f "start_http_server.py" ]; then
    print_error "start_http_server.py not found!"
    exit 1
fi

if [ ! -f "web_client.html" ]; then
    print_error "web_client.html not found!"
    exit 1
fi

# Check and kill existing processes on our ports
if check_port $WS_PORT; then
    print_warning "Port $WS_PORT is already in use"
    kill_port $WS_PORT
fi

if check_port $HTTP_PORT; then
    print_warning "Port $HTTP_PORT is already in use"
    kill_port $HTTP_PORT
fi

# Display network information
print_info "Local IP Address: ${GREEN}$LOCAL_IP${NC}"
echo ""

# Start WebSocket server
print_info "Starting WebSocket server on port $WS_PORT..."
python3 websocket_server.py > websocket.log 2>&1 &
WS_PID=$!

# Wait and check if WebSocket server started successfully
sleep 2
if kill -0 $WS_PID 2>/dev/null; then
    print_success "WebSocket server running (PID: $WS_PID)"
else
    print_error "Failed to start WebSocket server"
    cat websocket.log
    exit 1
fi

# Start HTTP server
print_info "Starting HTTP server on port $HTTP_PORT..."
python3 start_http_server.py > http.log 2>&1 &
HTTP_PID=$!

# Wait and check if HTTP server started successfully
sleep 2
if kill -0 $HTTP_PID 2>/dev/null; then
    print_success "HTTP server running (PID: $HTTP_PID)"
else
    print_error "Failed to start HTTP server"
    cat http.log
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════"
echo -e "${GREEN}         ✓ All Servers Running Successfully!${NC}"
echo "═══════════════════════════════════════════════════════"
echo ""
echo -e "${YELLOW}📱 ACCESS FROM YOUR PHONE:${NC}"
echo "───────────────────────────────────────────────────────"
echo -e "  1. Make sure your phone is on the ${BLUE}same WiFi${NC}"
echo -e "  2. Open browser on your phone"
echo -e "  3. Go to: ${GREEN}http://$LOCAL_IP:$HTTP_PORT/web_client.html${NC}"
echo -e "  4. Click the ${CYAN}'Connect'${NC} button"
echo "───────────────────────────────────────────────────────"
echo ""
echo -e "${YELLOW}💻 ACCESS FROM THIS COMPUTER:${NC}"
echo "───────────────────────────────────────────────────────"
echo -e "  • Web Client: ${GREEN}http://localhost:$HTTP_PORT/web_client.html${NC}"
echo -e "  • Python Test: ${CYAN}python3 client_example.py${NC}"
echo "───────────────────────────────────────────────────────"
echo ""
echo -e "${YELLOW}📊 SERVER STATUS:${NC}"
echo "───────────────────────────────────────────────────────"
echo -e "  • WebSocket Server: ${GREEN}ws://$LOCAL_IP:$WS_PORT${NC} (PID: $WS_PID)"
echo -e "  • HTTP Server:      ${GREEN}http://$LOCAL_IP:$HTTP_PORT${NC} (PID: $HTTP_PID)"
echo "───────────────────────────────────────────────────────"
echo ""
echo -e "${YELLOW}📝 LOGS:${NC}"
echo "───────────────────────────────────────────────────────"
echo -e "  • WebSocket: ${CYAN}tail -f websocket.log${NC}"
echo -e "  • HTTP:      ${CYAN}tail -f http.log${NC}"
echo "───────────────────────────────────────────────────────"
echo ""
echo -e "${RED}Press Ctrl+C to stop all servers${NC}"
echo ""

# Keep script running and show live WebSocket logs
tail -f websocket.log
