#!/usr/bin/python3
"""
Python script to expose a REST API
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import os
import psutil

HOSTNAME = '127.0.0.1'
HOSTPORT = 9000

class RESTSERVER(BaseHTTPRequestHandler):
    """
    Creating a webserver
    """
    def do_GET(self): # pylint: disable=invalid-name
        """
        Enable get method
        """
        if self.path == "/metrics":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            cpu_percent = psutil.cpu_percent()
            cpu_count = psutil.cpu_count()
            mem_available = psutil.virtual_memory().available / (1024.0 ** 3)
            mem_percent = psutil.virtual_memory().percent
            metrics = json.dumps({
                'cpu': {'cpu percent': cpu_percent, 'cpu count': cpu_count},
                'memory': {'memory percent': mem_percent, 'memory available (GB)': mem_available}
            }, indent=4, sort_keys=True)
            self.wfile.write(metrics.encode())

        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            puttest = os.popen("./check-put.sh").read()
            if puttest != 'error\n':
                indexfile = './model-ok.html'
                index = open(indexfile, 'r')
                i = index.read()
                self.wfile.write(bytes(i, "utf-8"))
            else:
                indexfile = './model-error.html'
                index = open(indexfile, 'r')
                i = index.read()
                self.wfile.write(bytes(i, "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))


RESTSERVER = HTTPServer((HOSTNAME, HOSTPORT), RESTSERVER)
print(time.asctime(), "Server Starts - %s:%s" % (HOSTNAME, HOSTPORT))

try:
    RESTSERVER.serve_forever()
except KeyboardInterrupt:
    pass

RESTSERVER.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (HOSTNAME, HOSTPORT))
