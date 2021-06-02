#!/usr/bin/env python3
#
# This is the solution code for the *echo server*.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


class LoginHandler(BaseHTTPRequestHandler):
    # get_method로 들어온 모든 request를 받는다. post는 do_post인가??
    # 이함수를 오버라이딩 해주어야 한다.
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # print(parts) 하면 아래와 같이 출력됨
        #    (url이 'https://www.google.com/search?q=gray+squirrel&tbm=isch' 인 경우)
        #     ParseResult(scheme='https', netloc='www.google.com', path='/search',
        #                   params='', query='q=gray+squirrel&tbm=isch', fragment='')
        parts = urlparse(self.path)
        try:
            # q = dict([p.split('=') for p in parts[4].split('&')])
            # '&'를 기준으로 문자열을 나누어주고, 그 후 '='로 나누어 주고 key, value로써 q에 저장한다.
            # parts.query 부분에서 원하는 query string을 읽어온다.
            q = dict([p.split('=') for p in parts.query.split('&')])
        except:
            q = {}
        for k in q.keys() :
            # parsing 한대로 request를 보내준다.
            # wfile.write는 데이터를 서버에 전송하는 코드이다.
            self.wfile.write((k + ' = ' + q[k] + '\n').encode())


if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, LoginHandler)
    httpd.serve_forever()
