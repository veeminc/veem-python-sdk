# Standard library imports...
import os
import six
import yaml
import socket
import logging
import requests

if six.PY3:
    # python 3 import
    from http.server import BaseHTTPRequestHandler, HTTPServer
    from urllib import parse as urlparse
else:
    # python 2 import
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
    from urlparse import urlparse


def str_to_bytes(text):
    if six.PY3: return bytes(text, 'utf8')
    return bytes(text)

logger = logging.getLogger(__name__)

class MockServerRequestHandler(BaseHTTPRequestHandler):

    def __init__(self, *args, **kwargs):
        mock_payload_file = os.path.join(
                                os.path.dirname(os.path.realpath(__file__)),
                                'yamls',
                                'mock_server_payload.yaml')
        with open(mock_payload_file, 'r') as stream:
            try:
                self.payload = yaml.safe_load(stream) or {}
            except yaml.YAMLError as exc:
                logger.error(exc)

        self.get_payload = self.payload.get('get', {})
        self.post_payload = self.payload.get('post', {})
        self.patch_payload = self.payload.get('patch', {})
        self.put_payload = self.payload.get('put', {})
        super().__init__(*args, **kwargs)

    def do_GET(self):
        # Process an HTTP GET request and return a response with a 200 status.
        self.send_response(requests.codes.ok)
        self.end_headers()
        path = urlparse.urlparse(self.path).path
        self.wfile.write(str_to_bytes(self.get_payload.get(path, '{}')))

    def do_POST(self):
        # Process an HTTP POST request and return a response with a 200 status.
        self.send_response(requests.codes.ok)
        self.end_headers()
        path = urlparse.urlparse(self.path).path
        self.wfile.write(str_to_bytes(self.post_payload.get(path, '{}')))

    def do_PATCH(self):
        # Process an HTTP PATCH request and return a response with a 200 status.
        self.send_response(requests.codes.ok)
        self.end_headers()
        path = urlparse.urlparse(self.path).path
        self.wfile.write(str_to_bytes(self.patch_payload.get(path, '{}')))

    def do_PUT(self):
        # Process an HTTP PUT request and return a response with a 200 status.
        self.send_response(requests.codes.ok)
        self.end_headers()
        path = urlparse.urlparse(self.path).path
        self.wfile.write(str_to_bytes(self.put_payload.get(path, '{}')))

    def do_DELETE(self):
        # Process an HTTP DELETE request and return a response with a 200 status.
        self.send_response(requests.codes.ok)
        self.end_headers()

class MockServerProcess(object):

    def __init__(self):
        s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM)
        s.bind(('localhost', 0))
        _, self.port = s.getsockname()
        s.close()
        logger.info('blinds to port: {}'.format(self.port))

    def start(self):
        mock_server = HTTPServer(('localhost', self.port),
                                 MockServerRequestHandler)
        while True:
            mock_server.handle_request()
