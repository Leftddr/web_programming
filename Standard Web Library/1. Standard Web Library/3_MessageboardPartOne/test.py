#!/usr/bin/env python3
#
# Test script for the Messageboard Part One server.
#
# The server should be listening on port 8000 and answer a POST request
# with an echo of the "message" field.

# request는 post, get등을 이용해 요청을 보내보는 모듈이다.
import requests, random, socket

# 서버가 열려 있는지 확인하는 함수이다.
def test_connect():
    '''Try connecting to the server.'''
    print("Testing connecting to the server.")
    try:
        # socket을 이용하여 연결을 시도한다. localhost의 8000번에..
        with socket.socket() as s:
           s.connect(("localhost", 8000))
        print("Connection attempt succeeded.")
        return None
    except socket.error:
        return "Server didn't answer on localhost port 8000.  Is it running?"

def test_POST():
    '''The server should accept a POST and return the "message" field.'''
    print("Testing POST request.")
    mesg = random.choice(["Hi there!", "Hello!", "Greetings!"])
    uri = "http://localhost:8000/"
    try:
        # post 방식이므로 data에 값을 실어서 보낸다.
        r = requests.post(uri, data = {'message': mesg})
    except requests.RequestException as e:
        return ("Couldn't communicate with the server. ({})\n"
                "If it's running, take a look at its output.").format(e)
    if r.status_code == 501:
        return ("The server returned status code 501 Not Implemented.\n"
                "This means it doesn't know how to handle a POST request.\n"
                "(Is the correct server code running?)")
    elif r.status_code != 200:
        return ("The server returned status code {} instead of a 200 OK."
                ).format(r.status_code)
    elif r.text != mesg:
        return ("The server sent a 200 OK response, but the content differed.\n"
                "I expected '{}' but it sent '{}'.").format(mesg, r.text)
    else:
        print("POST request succeeded.")
        return None


if __name__ == '__main__':
    tests = [test_connect, test_POST]
    for test in tests:
        problem = test()
        if problem is not None:
            print(problem)
            break
    if not problem:
        print("All tests succeeded!")
