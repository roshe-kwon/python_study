# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법 --> 매우 중요

from http.client import responses
import urllib.request as req
from urllib.error import URLError, HTTPError  # 주소가 잘못된 경우

# 다운로드 경로 및 파일명

path_list = ["C:/test1.jpg", "C:/index.html"]

# 다운로드 리소스 url
target_url = ["https://img1.daumcdn.net/thumb/R800x0/?scode=mtistory2&fname=https%3A%2F%2Ft1.daumcdn.net%2Fcfile%2Ftistory%2F2408DD3658A648B12C", "http://naver.com"]

for i, url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용
        contents = response.read()

        print("----------------------------------------")

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print("----------------------------------------")

        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("Download failed.")
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("Download failed.")
        print("URLError Reason : ", e.reason)

    # 성공
    else:
        print()
        print("Download Succeed.")
