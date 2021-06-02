#!/usr/bin/env python3
#
# Step one in building the messageboard server:
# An echo server for POST requests.

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs


class MessageHandler(BaseHTTPRequestHandler):
    # post 메소드가 나온다.
    def do_POST(self):
        # 1. How long was the message?
        # headers.get은 request로 온 모든 정보가 담겨 있다.
        length = int(self.headers.get('Content-length', 0))

        # 2. Read the correct amount of data from the request.
        # encode 해서 보냈으므로, decode해서 읽는다.
        # self.rfile을 이용해 내용물을 읽는다.
        data = self.rfile.read(length).decode()

        # 3. Extract the "message" field from the request data.
        # query_string을 parsing 한다. message의 0번째 값을 읽어온다.
        # 배열형태로 return이 되므로 0을 넣어서 값을 읽어온다.
        # html의 값을 읽어온다.
        message = parse_qs(data)["message"][0]

        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        #message를 encode해서 보내준다.
        #이 코드는 출력한 것을 의미한다.
        self.wfile.write(message.encode())

if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
