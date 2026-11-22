#!/usr/bin/env python3
"""Serve the two study libraries on loopback only, without exposing sibling folders."""
import argparse
import functools
import http.server
import json
from pathlib import Path
import socket
import urllib.parse
import urllib.request
import webbrowser

repository = Path(__file__).resolve().parents[2]
base = repository.parent
roots = {name: (base/name).resolve() for name in ('HFT_Docs', 'the_learning_curve') if (base/name/'index.html').is_file()}

def allowed(path):
    import re
    return not any(part.startswith('.') or re.sub(r'[^a-z0-9]', '', part.lower()) in {'mynotes','notes','90personalnotes','98archive','99buildartifacts'} for part in path.parts)

class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, '.mjs':'text/javascript', '.js':'text/javascript', '.wasm':'application/wasm', '.bcmap':'application/octet-stream', '.ftl':'text/plain'}

    def translate_path(self, path):
        parts = Path(urllib.parse.unquote(urllib.parse.urlsplit(path).path).lstrip('/')).parts
        if not parts or parts[0] not in roots or not allowed(Path(*parts[1:])):
            return str(base/'__not_served__')
        root = roots[parts[0]]
        candidate = root.joinpath(*parts[1:]).resolve()
        try: relative = candidate.relative_to(root)
        except ValueError: return str(base/'__not_served__')
        return str(candidate) if allowed(relative) else str(base/'__not_served__')

    def list_directory(self, path):
        self.send_error(404, 'Directory listing is disabled')
        return None

    def do_GET(self):
        if self.path == '/__library_status':
            body=json.dumps({'service':'study-library','roots':{k:str(v) for k,v in roots.items()}}).encode()
            self.send_response(200);self.send_header('Content-Type','application/json');self.send_header('Content-Length',str(len(body)));self.end_headers();self.wfile.write(body)
            return
        super().do_GET()

    def end_headers(self):
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def log_message(self, format, *args):
        if args and str(args[1] if len(args)>1 else '') not in ('200','304'):
            super().log_message(format,*args)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--no-browser',action='store_true')
    parser.add_argument('--port',type=int,default=8765)
    args=parser.parse_args()
    for port in range(args.port,args.port+10):
        address=f'http://127.0.0.1:{port}'
        try:
            with urllib.request.urlopen(address+'/__library_status',timeout=.3) as response:
                info=json.load(response)
            if info=={'service':'study-library','roots':{k:str(v) for k,v in roots.items()}}:
                url=address+'/'+repository.name+'/index.html'
                print('Library already running: '+url,flush=True)
                if not args.no_browser:webbrowser.open(url)
                return
        except Exception:pass
        try: server=http.server.ThreadingHTTPServer(('127.0.0.1',port),Handler)
        except OSError:continue
        url=address+'/'+repository.name+'/index.html'
        print('Study library: '+url+'\nKeep this window open while reading. Press Control-C to stop.',flush=True)
        if not args.no_browser:webbrowser.open(url)
        try:server.serve_forever()
        except KeyboardInterrupt:print('\nLibrary stopped.')
        finally:server.server_close()
        return
    raise SystemExit('No local port available; close an older library launcher and try again.')

if __name__=='__main__':main()
