import os
import http

import fire
import http.server
import socketserver

from generater import G


class Manager(object):
    """ Command line interface class """

    def generate(self, site_path, force=True):
        """ generate web pages """
        if not force:
            Q = "This will clear all existing files in the path {}, sure? ([yes]/no)".format(site_path)
            reply = input(Q)
            if reply == 'no':
                raise SystemExit
        g = G(site_path)
        g.gen_index()

    def server(self, site_path, port=8000):
        """ launch server """
        handler = http.server.SimpleHTTPRequestHandler
        
        os.chdir(site_path)
        with socketserver.TCPServer(("", port), handler) as httpd:
            print("serving at port", port)
            httpd.serve_forever()


if __name__ == "__main__":
    fire.Fire(Manager)