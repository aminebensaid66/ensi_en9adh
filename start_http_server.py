#!/usr/bin/env python3
"""
Simple HTTP server to serve the web client HTML file
Run this so you can access the WebSocket client from your phone
"""
import http.server
import socketserver
import os
import socket

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def log_message(self, format, *args):
        # Custom log format
        print(f"[HTTP] {self.address_string()} - {format % args}")

def get_local_ip():
    """Get the local IP address"""
    try:
        # Create a socket to get the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

def main():
    local_ip = get_local_ip()
    
    with socketserver.TCPServer(("0.0.0.0", PORT), MyHTTPRequestHandler) as httpd:
        print(f"HTTP Server running on port {PORT}")
        print(f"Local access: http://localhost:{PORT}/web_client.html")
        print(f"Network access: http://{local_ip}:{PORT}/web_client.html")
        httpd.serve_forever()

if __name__ == "__main__":
    main()
