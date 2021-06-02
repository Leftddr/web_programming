#!/usr/bin/env python3
#
# Client for the UINames.com service.

import requests


def SampleRecord():
    # http://citibikenyc.com/stations/json을 실행하면 json data를 return함.
    # get 요청을 보낸다.
    r = requests.get("http://citibikenyc.com/stations/json", timeout=2.0)

    # requests.get 메소드에서 return된 r은 JSON format data인데,
    # json()메소드를 실행하면, dictionary data type으로 변환 (j는 dictionary data type)
    # 파이썬에 맞게 dictionary 자료구조로 변환한다.
    j = r.json()
    # 첫번째 station 객체 가져옴
    station = j['stationBeanList'][0]

    return "Station name is {}, Number of Available Bykes {} and total number of Bykes is {}.".format(
        station["stationName"],
        station["availableDocks"],
        station["totalDocks"]
    )

if __name__ == '__main__':
    print(SampleRecord())
