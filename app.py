#!/usr/bin/env python

import textwrap, os

from six.moves.BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


class HelloRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path != '/':
            self.send_error(404, "Object not found")
            return
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        response_text = """<html>
                               <head>
                                   <title>Python Hello World!</title>
                               </head>
                               <body>
                                   <h3>Python Hello World!</h3>
                                   <br/>
                                   My hostname is """

        response_text = response_text + os.environ.get('HOSTNAME')
          
        response_text = response_text + "</body></html>"

        self.wfile.write(response_text.encode('utf-8'))


server_address = ('', 8080)
httpd = HTTPServer(server_address, HelloRequestHandler)
httpd.serve_forever()